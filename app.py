from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/cadastrar')
def cadastrar_servico():
    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)
