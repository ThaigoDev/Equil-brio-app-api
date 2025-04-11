from flask import Flask, render_template, request, redirect, url_for
from models.models import db
from models.forms import CadastroForm
from models.user import User
from config import Config

from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object(Config)

# Banco de dados
db.init_app(app)

# Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Cria tabelas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            login_user(user)
            return redirect(url_for('servicos'))
        else:
            return "Login inválido"

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha_hash = generate_password_hash(form.senha.data)

        if User.query.filter_by(email=email).first():
            return "Usuário já cadastrado!"

        novo_user = User(nome=nome, email=email, senha=senha_hash)
        db.session.add(novo_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('cadastro.html', form=form)

@app.route('/servicos')
@login_required
def servicos():
    return render_template('servicos.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
@login_required
def cadastrar_servico():
    form = CadastroServicoForm()
    if form.validate_on_submit():
        novo_servico = Servico(
            titulo=form.titulo.data,
            descricao=form.descricao.data,
            categoria=form.categoria.data,
            usuario_id=current_user.id
        )
        db.session.add(novo_servico)
        db.session.commit()
        return redirect(url_for('servicos'))
    return render_template('cadastrar.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
