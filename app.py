from flask import Flask, render_template, request, redirect, url_for, flash
from models import salvar_contato
from models import listar_contatos

app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret'


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

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        mensagem = request.form["mensagem"]

        if not nome or not email or not mensagem:
            flash("Preencha todos os campos!", "error")
        else:
            salvar_contato(nome, email, mensagem)
            flash("Mensagem enviada com sucesso!", "success")
            return redirect(url_for("contato"))

    return render_template("contato.html")

@app.route("/admin/contatos")
def admin_contatos():
    contatos = listar_contatos()
    return render_template("admin_contatos.html", contatos=contatos)

<<<<<<< HEAD


if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 7f463d1f7b7e739de5bb5f42b2220c0079c800fd
    app.run(debug=True)
