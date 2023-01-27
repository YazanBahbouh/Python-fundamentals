from flask_app import app
from flask import render_template, request, redirect, session

# Public Routes
@app.route('/')
def index():        
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')


# Hidden Routes
@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')