import re
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Secret Tunnel"

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/submission', methods=['POST'])
def surveyInput():
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['program'] = request.form['program']
    return redirect('/result')

@app.route('/result')
def result():
    if 'name' not in session:
        return redirect('/')
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)