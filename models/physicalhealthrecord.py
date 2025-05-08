class PhysicalHealthRecord(db.Model):
    __tablename__ = 'physical_health_records'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    weight = db.Column(db.Numeric(5, 2))
    height = db.Column(db.Numeric(4, 2))
    heart_rate = db.Column(db.Integer)
    sleep_hours = db.Column(db.Numeric(4, 2))
    exercise_minutes = db.Column(db.Integer)
    recorded_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
