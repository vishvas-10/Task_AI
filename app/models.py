from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    initials = db.Column(db.String(2), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False) 

    # Relationships: This allows to do user.tasks or user.stats
    tasks = db.relationship('Tasks', backref='owner', lazy=True)
    stats = db.relationship('Stats', backref='user', uselist=False) # One-to-one

class Stats(db.Model):
    # Added ForeignKey so DB knows which user these stats belong to
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    active_tasks = db.Column(db.Integer, default=0)
    completed_tasks = db.Column(db.Integer, default=0)
    productivity = db.Column(db.Integer, default=0)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    ai_generated = db.Column(db.Boolean, default=False)
    priority = db.Column(db.String(10), default="medium")
    
    # Relationship to subtasks
    subtasks = db.relationship('Subtasks', backref='parent_task', lazy=True)

class Subtasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Added ForeignKey to link to the parent Task
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    importance = db.Column(db.String(10))
    urgency = db.Column(db.String(20))
