import socket as sck

HOST = "192.168.10.121"
PORT = 5050

c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
c.connect(("192.168.10.121", 5050))

N = 9973
g = 1567
a = int(input("Inserire a ---> 1 < a < N --> "))

A = (g**a)%N
c.sendall(str(A).encode())
print(f"Invio a Bruno/Bob A --> {A}")
B = int(c.recv(4096).decode())
print(f"Ricevo da Bruno/Bob B --> {B}")
k = (B**a)%N
print(f"Stampo k --> {k}")

c.close()