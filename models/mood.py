class Mood(db.Model):
    __tablename__ = 'moods'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    note = db.Column(db.Text)
    recorded_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
