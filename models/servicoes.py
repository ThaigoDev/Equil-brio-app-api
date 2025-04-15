from sqlalchemy import Column, Integer, String, ForeignKey, Text, DECIMAL
from sqlalchemy.orm import relationship
from models import db

class Servico(db.Model):
    __tablename__ = 'servicos'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    categoria = Column(String(50), nullable=True)
    preco = Column(DECIMAL(10, 2), nullable=True)
    localizacao = Column(String(100), nullable=True)
    
    # Chave estrangeira para a tabela de usuários
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)  # Chave estrangeira

    # Relacionamento para acessar o usuário do serviço
    usuario = relationship('User', backref='servicos')  # Relacionamento com a tabela User

    def __repr__(self):
        return f'<Servico {self.titulo}>'
