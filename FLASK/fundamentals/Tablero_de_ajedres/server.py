from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template("index.html")

@app.route('/<x>/<y>')
def play_variables(x, y):
    return render_template("index2.html", x =  int(x), y =  int(y))

if __name__=="__main__":  
    app.run(debug=True)