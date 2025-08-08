from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("nisesilveira.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/nisesilveira")
def nisesilveira():
    return render_template("nisesilveira.html")


if __name__ == "__main__":
    app.run(debug=True)
