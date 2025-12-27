from flask import Blueprint, render_template, session, redirect,url_for, request, jsonify
from app import db
from datetime import datetime
from app.models import User, Stats, Tasks, Subtasks
from app.forms.task_form import Task_Form
from app.services.subtask_generator import generate_subtasks
from app.decorators import is_authenticated

tasks_bp = Blueprint('tasks',__name__)


def get_stats_data(user_id):
    from app.models import User
    curr_user = User.query.get(user_id)
    
    if not curr_user:
        return {"active_tasks": 0, "completed_tasks": 0, "productivity": 0}

    # Your original logic applied to the helper function
    total_subtasks = sum(len(t.subtasks) for t in curr_user.tasks)
    completed_subtasks = sum(1 for t in curr_user.tasks for s in t.subtasks if s.completed)
    
    active_tasks_count = len([t for t in curr_user.tasks if not t.completed])
    completed_tasks_count = len([t for t in curr_user.tasks if t.completed])
    
    # Calculate productivity based on subtasks as per your reference
    productivity = int((completed_subtasks / total_subtasks) * 100) if total_subtasks > 0 else 0
    
    return {
        "active_tasks": active_tasks_count, 
        "completed_tasks": completed_tasks_count, 
        "productivity": productivity
    }


@tasks_bp.route('/add-task', methods = ["POST","GET"])
@is_authenticated
def add_task():
    form = Task_Form()
    
    if form.validate_on_submit(): #Check if the form is valid
        curr_user_id = session.get('user')
        
       
        new_task = Tasks(
            user_id=curr_user_id, 
            title=form.task.data, 
            completed=False
        )
        db.session.add(new_task)
        db.session.flush()
        subtasks = generate_subtasks(form.task.data)
        if 'priority' in subtasks:
            new_task.priority=subtasks["priority"]
        if "result" in subtasks and subtasks["result"] == "successful":
            new_task.ai_generated=True
            for subtask in subtasks["subtasks"]:
                new_subtask = Subtasks(
                    task_id=new_task.id,
                    title=subtask["task"],
                    importance=subtask["importance"],
                    urgency=subtask["urgency"]
                    )
                db.session.add(new_subtask)    
        db.session.commit()

        return redirect(url_for('dashboard.dashboard'))
    print(form.errors)
    return redirect(url_for('dashboard.dashboard'))



@tasks_bp.route('/delete-task', methods = ["POST"])
@is_authenticated
def delete_task():
  
    data = request.get_json()
    task_id = data.get('task_id')

    if not task_id:
        return jsonify({'success': False, 'error': 'No task ID provided'}), 400

    
    task_to_delete = Tasks.query.get(task_id)
    
    if task_to_delete:
        if task_to_delete.user_id != session["user"]:
            return jsonify({'success': False, 'error': 'Unauthorized'}), 403
        Subtasks.query.filter_by(task_id=task_id).delete()
        db.session.delete(task_to_delete)
        db.session.commit()
        
        return jsonify({'success': True,})
    else:
        return jsonify({'success': False, 'error': 'Task not found'}), 404


@tasks_bp.route('/toggle-task', methods=["POST"])
@is_authenticated
def toggle_task():
    data = request.get_json()
    task_id = data.get('task_id')
    
    if not task_id:
        return jsonify({'success': False, 'error': 'No task ID provided'}), 400
    
    task = Tasks.query.get(task_id)
    if not task or task.user_id != session.get('user'):
        return jsonify({'success': False, 'error': 'Unauthorized or Not Found'}), 403

    # Toggle logic: If task is completed, make it False (and vice versa)
    new_state = not task.completed
    task.completed = new_state
    
    # Sync all subtasks to the parent task state
    Subtasks.query.filter_by(task_id=task_id).update({Subtasks.completed: new_state})
    
    db.session.commit()

    # Get fresh stats for the user
    stats_raw = get_stats_data(session.get('user'))
    
    # Render ONLY the stats part of the page
    # Note: Use the variable names expected by your dashboard (e.g., 'stats')
    stats_html = render_template('_stats_partial.html', stats=stats_raw)

    return jsonify({
        'success': True, 
        'stats_html': stats_html,
        'active_count': stats_raw['active_tasks'],
        'stats': stats_raw
    })
    
@tasks_bp.route('/toggle-subtask', methods=["POST"])
@is_authenticated
def toggle_subtask():
    data = request.get_json()
    subtask_id = data.get('subtask_id')
    
    if not subtask_id:
        return jsonify({'success': False, 'error': 'No subtask ID provided'}), 400
    
    subtask = Subtasks.query.get(subtask_id)
    if not subtask:
        return jsonify({'success': False, 'error': 'Subtask not found'}), 404
        
    # Security check: Ensure the parent task belongs to the current user
    parent_task = Tasks.query.get(subtask.task_id)
    if not parent_task or parent_task.user_id != session.get('user'):
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403

    # Toggle the completion state
    subtask.completed = not subtask.completed
    db.session.commit()
    
    # Get fresh stats and render the partial
    stats_raw = get_stats_data(session.get('user'))
    stats_html = render_template('_stats_partial.html', stats=stats_raw)
    
    return jsonify({
        'success': True,
        'stats_html': stats_html,
        'active_count': stats_raw['active_tasks'],
        'stats': stats_raw
    })