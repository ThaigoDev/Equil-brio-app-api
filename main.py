from flask import Flask, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from database.db_setup import db
import os
from dotenv import load_dotenv

load_dotenv()

# Inicialização do Flask
app = Flask(__name__)

# Configuração para PostgreSQL (Render)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do banco de dados
db.init_app(app)

# Importa os modelos e rotas
from models.user import User
from routes.api_routes import *

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
