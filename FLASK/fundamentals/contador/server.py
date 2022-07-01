from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'admin'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    print(session['count'])
    return render_template("index.html", count = session['count'])

@app.route('/add')
def add():
#BONUS NINJA: agrega un botón +2 debajo del contador y una nueva ruta que incremente el contador en 2
    session['count'] += 1 #0
    print(session['count'])
    return redirect("/")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)