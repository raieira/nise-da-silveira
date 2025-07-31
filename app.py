from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", css_file="estilo_home.css")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html", css_file="estilo_sobre.css")

if __name__ == "__main__":
    app.run(debug=True)