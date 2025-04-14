from flask_sqlalchemy import SQLAlchemy
from models import db  # usa o db da instância já configurada
from flask_login import UserMixin
from models.user import User

class Servico(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    usuario = db.relationship('User', backref=db.backref('servicos', lazy=True))
