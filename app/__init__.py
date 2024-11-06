from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "app"
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('blog.html', username = username)  #response to a form submission
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('create.html', username = username)  #response to a form submission
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('edit.html', username = username)  #response to a form submission
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('entry.html', username = username)  #response to a form submission
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('login.html', username = username)  #response to a form submission
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('reading.html', username = username)  #response to a form submission
def authenticate():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('rename.html', username = username)  #response to a form submission
app.run()
