from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resultado', methods=['POST'])
def result():
    print("--POST INFO OBTAINED--")
    print("Nombre:", request.form['name'])
    print("Localizacion:", request.form['location'])
    print("Lenguaje Favorito:", request.form['language'])
    print("Comentario:", request.form['comment'])
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    return render_template("resultado.html", name = name, location = location, language = language, comment = comment)

@app.route('/Peligro', methods=['GET'])
def danger():
    print("Una usuario(a) intentó visitar /Peligro.  Hemos redirigido al usuario a /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)