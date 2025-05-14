from database.db_setup import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    moods = db.relationship('Mood', backref='user', cascade="all, delete-orphan")
    physical_health_records = db.relationship('PhysicalHealthRecord', backref='user', cascade="all, delete-orphan")
    habits = db.relationship('Habit', backref='user', cascade="all, delete-orphan")
    user_achievements = db.relationship('UserAchievement', backref='user', cascade="all, delete-orphan")
    progress_reports = db.relationship('ProgressReport', backref='user', cascade="all, delete-orphan")
