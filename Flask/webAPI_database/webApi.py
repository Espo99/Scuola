import flask
import sqlite3
from flask import request
from flask import jsonify

app = flask.Flask(__name__)
app.config["debug"] = True

@app.route('/',methods=["GET"])
def home():
   return "<h1>Biblioteca online con database</h1>"

@app.route('/allBooks', methods=["GET"])
def getAllBooks():
    try:
        sqliteConnection = sqlite3.connect('LibriDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM libri")
        allBooks = cursor.fetchall()

        print("eseguito")
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()
    return jsonify(allBooks)
   
@app.route('/bookById', methods=["GET"])
def searchById():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: no id field provided. Please specify an id"

    try:
        sqliteConnection = sqlite3.connect('LibriDB.db')
        cursor = sqliteConnection.cursor()

        cursor.execute(f"SELECT * FROM libri where id=={id}")
        book = cursor.fetchall()

        print("eseguito")
        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("eccezione --> " + error)

    finally:
        if (sqliteConnection):
            print('chiusura connessione con database')
            sqliteConnection.close()
    return jsonify(book)

app.run()