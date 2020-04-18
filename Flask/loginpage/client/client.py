import hashlib
import socket 
import flask

def getHash(string):
    m = hashlib.sha256()
    m.update(string)
    return m.hexdigest()

IP = "192.168.10.73"
PORT = 5000
method = "POST"
URL = "http://127.0.0.1:5000/register"
version = "HTTP/1.0"
username = "user"
password = getHash("123456")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     
s.connect((IP,PORT))

body_entity = f"username={username}&password={password}"    

headers = f"Content-Type: application/x-www-form-urlencoded\nContent-Length: {len(body_entity)}" 

request = f"{method} {URL} {version}\n{headers}\n\n{body_entity}"   

s.send(request.encode())
out_file = open("file_post.html","w")  
data="none"
while data != "":
    data = s.recv(4096).decode()    
    out_file.writelines(data)       
    #print(data)
out_file.close()    

s.close()   