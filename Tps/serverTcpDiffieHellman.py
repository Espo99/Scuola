import socket as sck

HOST = "0.0.0.0"
PORT = 5050

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
con, addr =s.accept()

N = 9973
g = 1567


A = int(con.recv(4096).decode())
print(f"Ricevo da Alice A --> {A}")

b = int(input("Inserire b ---> 1 < b < N --> "))
B = (g**b)%N
con.sendall(str(B).encode())
print(f"Invio a Alice B --> {B}")
k = (A**b)%N
print(f"Stampo k --> {k}")
s.close()