from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.user import User
from models.servicoes import Servico
from models.forms import RegistroUsuarioForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-secreta-segura'

# Configuração para PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://12231:313131!@localhost:5433/teste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar a instância de LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'  # Rota para redirecionar usuários não autenticados

# Inicializar SQLAlchemy e LoginManager com a app Flask
db.init_app(app)
login_manager.init_app(app)

# Definir o loader de usuário
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Criando o banco de dados diretamente no bloco principal
with app.app_context():
    db.create_all()  # Cria todas as tabelas, se não existirem.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegistroUsuarioForm()
    if form.validate_on_submit():
        usuario_existente = User.query.filter_by(email=form.email.data).first()
        if usuario_existente:
            flash('E-mail já cadastrado.')
            return redirect(url_for('cadastro'))
        
        senha_hash = generate_password_hash(form.senha.data)
        novo_usuario = User(nome=form.nome.data, email=form.email.data, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Registro realizado com sucesso!')
        return redirect(url_for('login'))
    
    return render_template('cadastro_usuario.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = User.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            return redirect(url_for('servicos'))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/servicos')
@login_required
def servicos():
    servicos = Servico.query.all()
    return render_template('servicos.html', servicos=servicos)

@app.route('/cadastrar-servico', methods=['GET', 'POST'])
@login_required
def cadastrar_servico():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        categoria = request.form['categoria']

        novo_servico = Servico(
            titulo=titulo,
            descricao=descricao,
            categoria=categoria,
            usuario_id=current_user.id
        )
        db.session.add(novo_servico)
        db.session.commit()
        flash('Serviço cadastrado com sucesso!')
        return redirect(url_for('servicos'))
    
    return render_template('registrar_servico.html')

# Criando o banco de dados diretamente no bloco principal
with app.app_context():
    db.create_all()  # Cria todas as tabelas, se não existirem

if __name__ == '__main__':
    app.run(debug=True)


