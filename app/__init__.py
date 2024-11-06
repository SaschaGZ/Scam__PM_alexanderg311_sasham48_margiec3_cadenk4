from flask import Flask
from flask import render_template
from flask import session
from flask import request, flash, redirect
import sqlite3
app = Flask(__name__)

@app.route("/")
def login():
    print(__name__)
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    session['password'] = password
    return render_template("login.html")
@app.route("/blog")
def blog():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    return render_template('blog.html', username = username)  #response to a form submission
@app.route("/create")
def create():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    return render_template('create.html')  #response to a form submission
@app.route("/edit")
def edit():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    return render_template('edit.html', username = username)  #response to a form submission
@app.route("/entry")
def entry():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    return render_template('entry.html', username = username)  #response to a form submission
@app.route("/reading")
def reading():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    return render_template('reading.html', username = username)  #response to a form submission
@app.route("/rename")
def rename():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    session['username'] = username
    return render_template('rename.html', username = username)  #response to a form submission
    app.debug = True
    app.run()
