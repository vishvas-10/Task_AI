from flask import Blueprint, session, render_template
from app.models import User, Tasks,Subtasks,Stats
from app.forms.task_form import Task_Form
from datetime import datetime
from app.decorators import is_authenticated

dashboard_bp = Blueprint('dashboard',__name__)



@dashboard_bp.route('/dashboard')
@dashboard_bp.route('/dashboard/<status>')
@is_authenticated
def dashboard(status = 'all'):
    form = Task_Form()
    curr_user = User.query.get(session['user'])
    # Get greeting based on time
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    # Stats data
    total_subtasks = sum(len(t.subtasks) for t in curr_user.tasks)
    completed_subtasks = sum(1 for t in curr_user.tasks for s in t.subtasks if s.completed)
    stats = {
        'active_tasks': len([t for t in curr_user.tasks if not t.completed]),
        'completed_tasks': len([t for t in curr_user.tasks if t.completed]),
        'productivity': int((completed_subtasks / total_subtasks) * 100) if total_subtasks > 0 else 0
    }
    
    # Tasks data 
    if status == 'active':
        task_db = Tasks.query.filter_by(user_id = curr_user.id, completed = False ).all()
    elif status == 'completed':
        task_db = Tasks.query.filter_by(user_id = curr_user.id, completed = True ).all()
    else:
        task_db = curr_user.tasks
    
    return render_template('dashboard.html', 
                         user=curr_user, 
                         stats=stats, 
                         tasks=task_db,
                         greeting=greeting,
                         form=form)