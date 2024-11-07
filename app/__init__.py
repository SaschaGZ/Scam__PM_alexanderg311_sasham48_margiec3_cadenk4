from flask import Flask, render_template, session, request, redirect
import sqlite3
import key

app = Flask(__name__)
app.secret_key = key.key()

DB_FILE="scam_blog.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

c.execute("CREATE TABLE IF NOT EXISTS user_information (username TEXT UNIQUE, password TEXT)")

@app.route("/")
def login():
    if 'username' in session:
        user = session['username']
        return render_template('blog.html')
    return render_template("login.html")
@app.route("/auth", methods=['GET', 'POST'])
def auth():
    error = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        c.execute('SELECT password FROM user_information WHERE username = ?', (username,))
        match = c.fetchone()
        if match:
            if match[0] == password:
                session['username'] = username
                return redirect('/blog')
            else:
                error = "Incorrect password. Please try again."
                return redirect('/')
    return redirect('/create')
@app.route("/create", methods=['GET', 'POST'])
def create():
    error = ""
    if 'username' in session:
        user = session['username']
        return render_template('blog.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            c.execute('INSERT INTO user_information (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            session['username'] = username
            return render_template("blog.html")
        except sqlite3.IntegrityError:
            error = "Username already exists. Choose a different one."
            return render_template('create.html', error = error)
    return render_template('create.html')
@app.route("/edit")
def edit():
    return render_template('edit.html', username = username)
@app.route("/entry")
def entry():
    return render_template('entry.html', username = username) 
@app.route("/reading")
def reading():
    return render_template('reading.html', username = username)
@app.route("/rename")
def rename():
    return render_template('rename.html', username = username)
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    app.debug = True
    app.run()