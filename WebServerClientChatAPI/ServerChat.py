import flask
from flask import request, jsonify
import sqlite3
from datetime import datetime
import os
app = flask.Flask(__name__)
path_db = 'static/DBServerChat.db'    
@app.route('/api/v1/receive', methods=['GET'])
def messageForMe():     
    if (flask.request.method == 'GET'):
        if 'id_dest' in request.args:   
            dest = int(request.args['id_dest']) 
        try:
            sqliteConnection = sqlite3.connect(path_db)   
            cursor = sqliteConnection.cursor()
            cursor.execute(f"SELECT sender_id,text,receiver_id,timestamp FROM messaggi WHERE received=0  AND receiver_id = {dest}")
            anyMessage = cursor.fetchall()
            if len(anyMessage) != 0:   
                for ar in anyMessage:               
                    cursor.execute(f'''UPDATE messaggi 
                                        SET received = 1 
                                        WHERE messaggi.receiver_id = {ar[2]}''') 
                    sqliteConnection.commit() 
                if(len(res)==0):   
                    return []
            else:
                return []
        except sqlite3.Error as error:
            print("Error: " + error)

        finally:
            if (sqliteConnection):
                print('Chiusura connessione DB')
                sqliteConnection.close()
                return jsonify(anyMessage)  
@app.route('/', methods=['GET'])
def home():
    return "<h1>Chat</h1><p>Chat con Flask.</p>"
@app.route('/api/v1/user_list', methods=['GET'])
def api_all():
    try:
        sqliteConnection = sqlite3.connect(path_db)
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT * FROM utenti")  
        user = cursor.fetchall()
    except sqlite3.Error as error:
        print("Error: " + error)
@app.route('/api/v1/send', methods=['GET', 'POST'])
def api_send():
    if request.method == 'GET':
        if 'id_dest' in request.args and 'text' in request.args and 'id_mitt' in request.args:  
            dest = int(request.args['id_dest'])
            text = request.args['text']
            mitt = int(request.args['id_mitt'])
        else:
            return 'Error missing arguments'
        try:
            sqliteConnection = sqlite3.connect(path_db)   
            cursor = sqliteConnection.cursor()
            cursor.execute(f'''SELECT user_id
                                FROM utenti
                                WHERE user_id = {dest} or user_id = {mitt};''') 
            user = cursor.fetchall()
            if (len(user)>1):   
                date = datetime.now() 
                time = date.strftime("%H:%M:%S")    
                len_text = len(text)    
                cursor.execute(f'''
                    INSERT INTO messaggi(receiver_id, sender_id, timestamp, text, length, received) 
                    VALUES ({dest}, {mitt}, "{text}", "{time}", {len_text}, {False});''')  
                sqliteConnection.commit() 
            else:
                return 'Utenti non registrati'
        except sqlite3.Error as error:
            print('Error: ' + error)
if __name__== "__main__":  
    app.run(host="127.0.0.1", port=int(8080), debug=True)