from flask import Flask, render_template, request, redirect, url_for, flash
from models import init_db, add_contato

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret'

init_db()

@app.route('/')
def index():
    return render_template('index.html', page_title='Início')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', page_title='Sobre Nise da Silveira')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html', page_title='Serviços')

@app.route('/recursos')
def recursos():
    return render_template('recursos.html', page_title='Recursos')

@app.route('/blog')
def blog():
    return render_template('blog.html', page_title='Blog')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        mensagem = request.form.get('mensagem', '').strip()
        if not nome or not email or not mensagem:
            flash('Por favor, preencha todos os campos.', 'error')
            return redirect(url_for('contato'))
        flash('Mensagem enviada com sucesso! Entraremos em contato em breve.', 'success')
        return redirect(url_for('contato'))
    return render_template('contato.html', page_title='Contato')

if __name__ == '__main__':
    app.run(debug=True)
