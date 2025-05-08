class ProgressReport(db.Model):
    __tablename__ = 'progress_reports'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    report_type = db.Column(db.String(50), nullable=False)  # ex: "humor", "hábitos"
    data = db.Column(db.JSON, nullable=False)
    generated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
