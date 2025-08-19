from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db, add_contato

app = Flask(__name__)
app.secret_key = "supersecretkey"

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')
        if not nome or not email or not mensagem:
            flash("Todos os campos são obrigatórios!", "error")
            return redirect(url_for('contato'))
        add_contato(nome, email, mensagem)
        flash("Mensagem enviada com sucesso!", "success")
        return redirect(url_for('contato'))
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
