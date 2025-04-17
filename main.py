from flask import Flask, url_for, request, flash
import os
from flask_sqlalchemy import SQLAlchemy
from database.db_setup import db 
# Inicialização do Flask
app = Flask(__name__)

# Configuração para PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados
db.init_app(app)

# Importa os modelos após a configuração do banco de dados
from models.user import User

# Importa as rotas após a configuração do banco de dados
from routes.api_routes import  *

# Registrando o Blueprint


# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug= os.getenv("DEBUG"))
