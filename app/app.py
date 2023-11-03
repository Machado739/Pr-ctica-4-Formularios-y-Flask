from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates')

@app.route("/")
def inicio():
    return render_template("public/index.html")

# Crea rutas adicionales para las páginas adicionales de tu proyecto
@app.route("/index2")
def index2():
    return render_template("public/index2.html")

@app.route("/index3")
def index3():
    return render_template("public/index3.html")

@app.route("/index4")
def index4():
    return render_template("public/index4.html")

if __name__ == "__main__":
    app.run(debug=True)
