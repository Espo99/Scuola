import socket as sck
ADDRESS="0.0.0.0"
PORT=5432
s=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.bind((ADDRESS,PORT))
s.listen()
conn,address = s.accept()
print("Connesso con ", conn)
while True:
    data=conn.recv(4096).decode()
    print('\n > client %s: %s' %(address,data))
    strToSend=input(">>")
    conn.sendall(strToSend.encode())
    if(strToSend=='0'):
        break
conn.close()
s.close()