from flask import Flask, render_template

app = Flask(__name__)

# Rota 1: Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota 2: Página sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota 3: Página de contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota 4: Página de erro (para URLs inválidas)
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('erro.html'), 404

if __name__ == '__main__':
    app.run(debug=True)