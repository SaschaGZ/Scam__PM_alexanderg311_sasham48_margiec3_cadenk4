from flask import Flask
from flask import render_template
from flask import session
from flask import request, flash, redirect
import sqlite3
app = Flask(__name__)

DB_FILE="scam_blog.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#c.execute("CREATE TABLE user_information (username TEXT, password TEXT)")

@app.route("/")
def login():
    print(__name__)
    return render_template("login.html")
@app.route("/auth")
def blog():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.args['username']
        username = request.args['password']
        method = 'GET'
    c.execute('SELECT password FROM user_information WHERE username = ?', (username,))
    result = c.fetchone()

    if result:
        # Username exists, now check if the password matches
        if result[0] == password:
            session['username'] = username  # Store user in session
            return render_template('blog.html', username = username)  #response to a form submission
        else:
            flash("Incorrect password. Please try again.", "danger")
        return render_template('login.html')  #response to a form submission
    else:
        # Username does not exist, redirect to registration
        flash("Username not found. Please created account firs first.", "danger")
        return render_template('create.html')  #response to a form submission
@app.route("/create")
def create():
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
if __name__ == "__main__":
    app.debug = True
    app.run()
