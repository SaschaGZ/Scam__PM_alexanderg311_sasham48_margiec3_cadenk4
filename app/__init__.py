from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def login():
    print(__name__)
    return render_template("login.html")
@app.route("/blog")
def blog():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('blog.html', username = username)  #response to a form submission
@app.route("/create")
def create():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('create.html')  #response to a form submission
@app.route("/edit")
def edit():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('edit.html', username = username)  #response to a form submission
@app.route("/entry")
def entry():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('entry.html', username = username)  #response to a form submission
@app.route("/reading")
def reading():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('reading.html', username = username)  #response to a form submission
@app.route("/rename")
def rename():
    if request.method == 'POST':
        method = 'POST'
        username = request.form.get('username')
    else:
        username = request.args['username']
        method = 'GET'
    session['username'] = username
    return render_template('rename.html', username = username)  #response to a form submission
    app.debug = True
    app.run()
