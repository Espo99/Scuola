import socket as sck

IP_SVR="192.168.10.54"
ADDRESS="0.0.0.0"
PORT=8080

SckSrvr=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
SckSrvr.bind((ADDRESS,PORT))
SckSrvr.listen()
conn,address = SckSrvr.accept()

SckClnt=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
PORTT=int(input("Porta: "))
SckClnt.connect((IP_SVR,PORT))

strToSend=""

while True:
    data=conn.recv(4096).decode()
    print('\n > client %s: %s' %(address,data))
    strToSend=input(">>")
    conn.sendall(strToSend.encode())
    if(strToSend=='0'):
        break

    strToSend=input("\n>")
    if strToSend=="0":
        break
    SckClnt.sendall(strToSend.encode())
    data=SckClnt.recv(4096).decode()
    print("Server: %s" %data)

conn.close()
SckClnt.close()
SckSrvr.close()