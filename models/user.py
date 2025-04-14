# models/user.py
from flask_login import UserMixin
from models.models import db  # Corrigir a importação do db

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    # Adicionando o extend_existing=True para evitar o erro de redefinir a tabela
    __table_args__ = {'extend_existing': True}
