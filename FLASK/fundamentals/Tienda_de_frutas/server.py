from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import datetime

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pedido', methods=["POST"])
def checkout():
    print("--POST INFO OBTAINED--")
    print("Name:", request.form['name'])
    print("Student ID:", request.form['studentid'])
    print("Dojo:", request.form['dojo'])
    print("apples:", request.form['apples'])
    print("blackberry:", request.form['blackberry'])
    print("raspberry:", request.form['raspberry'])
    print("strawberry:", request.form['strawberry'])
   

    name = request.form['name']
    studentid = request.form['studentid']
    apples = request.form['apples']
    blackberry = request.form['blackberry']
    raspberry = request.form['raspberry']
    strawberry = request.form['strawberry']
  
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    return render_template("index2.html", name = name, studentid = studentid, apples = int(apples), blackberry = int(blackberry), raspberry = int(raspberry), strawberry = int(strawberry),  timestamp = timestamp)

if __name__=="__main__":
    app.run(debug=True)