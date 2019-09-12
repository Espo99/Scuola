import socket as sck 
s=sck.socket(sck.AF_INET,sck.SOCK_STREAM)
IP_SVR=input("Indirizzo server: ")
PORT=int(input("Porta: "))
s.connect((IP_SVR,PORT))
strToSend=""
while True:
    strToSend=input("\n>")
    if strToSend=="0":
        break
    s.sendall(strToSend.encode())
    data=s.recv(4096).decode()
    print("Server: %s" %data)
s.close()