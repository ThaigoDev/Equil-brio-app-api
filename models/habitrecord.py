class HabitRecord(db.Model):
    __tablename__ = 'habit_records'

    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.id'), nullable=False)
    completed_count = db.Column(db.Integer, nullable=False, default=0)
    recorded_date = db.Column(db.Date, nullable=False)
