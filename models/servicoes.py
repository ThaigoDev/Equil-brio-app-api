from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Servico(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)  # Correção aqui
    
    usuario = db.relationship('User', backref=db.backref('servicos', lazy=True))  # Relacionamento
