import hashlib
from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

def getHash(string):
    m = hashlib.sha256()
    m.update(string)
    return m.hexdigest()

def validate(username, password):
    completion = False
    with sqlite3.connect('static/db.db') as con:   
        cur = con.cursor()
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            dbUser = row[0]
            dbPass = row[1]
            if dbUser == username:
                completion = check_password(dbPass, password)
    return completion

def insertDB(username, password):
    with sqlite3.connect('./static/db.db') as con:
        cur = con.cursor()
        try:
            cur.execute(f'INSERT INTO USERS (USERNAME, PASSWORD) VALUES ("{username}", "{password}")')      
        except Exception:
            pass
        

def check_password(hashed_password, user_password):         
    return hashed_password == getHash(user_password)


@app.route('/', methods=['GET', 'POST'])
def signInOrSignUp():                                       
    if request.method == 'POST':
        if request.form['submit_button'] == 'Log-In':
            return redirect(url_for('login'))
        elif request.form['submit_button'] == 'Sign-Up':
            return redirect(url_for('register'))
        else:
            pass 
        
    return render_template('index.html', error = error)


@app.route('/login', methods=['GET', 'POST'])    
def login():
    error = None
    if request.method == 'POST':                
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)       
        if completion == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':                            
        username = request.form['username']
        password = request.form['password']
        insertDB(username, password)

    return render_template('register.html', error=error)

@app.route('/secret')       
def secret():
    return "This is a secret page!"

if __name__== "__main__":    
    app.run()