import flask
from flask import request, jsonify
import sqlite3
import requests
from threading import Thread 
import time
import sys
import os
stop_thread = False
URL = "http://127.0.0.1/api/v1/"    
MY_ID = 12                                  
path_db = "static/DBClientChat.db"                           
class ReceiveThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.connectionURL = URL + 'receive'
        self.PARAMS = {'id_dest' : MY_ID}
    def run(self):
        while True:
            if not stop_thread: 
                time.sleep(5)   
                r = requests.get(url = self.connectionURL, params=self.PARAMS)  
                data = r.json() 
                try:
                    sqliteConn = sqlite3.connect(path_db)   
                    cursor = sqliteConn.cursor()            
                    if len(data)!=0:                        
                        for da in data:
                            cursor.execute(f'''
                            SELECT bloccato
                            FROM utenti
                            WHERE user_id = {da[0]};''') 
                            
                            if(not cursor.fetchall()[0][0]):
                                cursor.execute(f'''
                                VALUES ("{da[3]}", {da[0]});''') 
                    sqliteConn.commit()     
                except sqlite3.Error as error:  
                    print("Error: " + error)
                finally:
                    if (sqliteConnection):
                        sqliteConnection.close()  
            else:
                break
def printMenu():
    print("0 - Esci")
    print("1 - Rubrica")
    print("2 - Ricevuti")
    print("3 - Invia")
    print("4 - Blocca/Sblocca")
def user_list():
    try:
        sqliteConn = sqlite3.connect(path_db)
        cursor = sqliteConnection.cursor()
        cursor.execute(f"SELECT * FROM utenti;")   
        data = cursor.fetchall()    
        for da in data:  
            if da[4]:    
                s = 'Sì'    
            else:
                s = 'No'
            print(f"ID: {da[0]} - Nome: {da[1]} - Cognome: {da[2]} - Nick: {da[3]} - Bloccato: {s}")    
    except sqlite3.Error as error:  
        print("Error: " + error)
    finally:
        if (sqliteConnection):    
            print('Chiusura connessione DB')
            sqliteConn.close()
def receivedMessages():
    try:
        sqliteConn = sqlite3.connect(path_db)   
        cursor = sqliteConnection.cursor()
        cursor.execute(f"SELECT Messaggi.text, utenti.nick FROM Messaggi, utenti WHERE utenti.user_id = Messaggi.IdMitt;") #query
        data = cursor.fetchall()
        for da in data:      
            print(f"Messaggio ricevuto : {da[1]} - Testo: {da[0]}")
        sqliteConnection.commit()
    except sqlite3.Error as error:  
        print("Error: " + error)
def sendMex():
    try:
        sqliteConnection = sqlite3.connect(path_db)
        cursor = sqliteConnection.cursor()
        nick = input('A chi invii messaggio? \n')
        choice = input('Che messaggio vuoi inviare? (f/t)') 
         if choice.lower() == 'f':
             pass
        elif choice.lower() == 't':
            cursor.execute(f"SELECT user_id FROM utenti WHERE nick = '{nick}';")    
            result = cursor.fetchall()
            if (len(result)==1):
                text = input('Digita messaggio che vuoi inviare: \n')    
                PARAMS={'id_dest':result[0][0], 'text':text.replace(" ", "+"), 'id_mitt':MY_ID} 
                r = requests.get(url=URL+'send', params=PARAMS)            
                if(r.status_code==200):
                    cursor.execute(f"INSERT INTO Messaggi_TX(text, IdDest) VALUES ('{text}', {result[0][0]});") 
                    print("Messaggio corretto")    
                else:
                    print("Errore invio")
            else:
                print("Errore inserimento nickname")
            sqliteConnection.commit()
        else:
            print('Scelta non valida')
    except sqlite3.Error as error:
        print("Error: " + error)
def bloccaSblocca():
    try:
        sqliteConnection = sqlite3.connect(path_db)
        cursor = sqliteConnection.cursor()

        user = input("Seleziona contatto: \n")  
        cursor.execute(f"SELECT bloccato FROM utenti WHERE nick = '{user}';")
        data = cursor.fetchall()    
        if not data[0][0]:          
            s = 'bloccato'
        else:
            s = 'sbloccato'
            cursor.execute(f'''UPDATE utenti 
                                    SET bloccato = {(data[0][0]+1)%2}
                                    WHERE nick = "{user}"''')   
            
        sqliteConnection.commit() 
    except sqlite3.Error as error:
        print("Error: " + error)
recThread = ReceiveThread()
recThread.start()
while True:
    printMenu()
    choice = int(input(">>")) 
    if choice == 0:
        break
    elif choice == 1:
        user_list()
    elif choice == 2:
        receivedMessages()
    elif choice == 3:
        sendMex()
    elif choice == 4:
        bloccaSblocca()
    else:
        pass
stop_thread = True
recThread.join()