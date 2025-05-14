class Achievement(db.Model):
    __tablename__ = 'achievements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    points_rewarded = db.Column(db.Integer, nullable=False, default=0)

 
    user_achievements = db.relationship('UserAchievement', backref='achievement', cascade="all, delete-orphan")
