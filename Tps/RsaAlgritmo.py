#Esposito Christian 5AROB 

import random 

def numeroPrimo():
    numero = random.randint(10, 100)
    t = 6
    cont = 4
    primo = True
    while True:
        for p in range(2, t//2):
            if(t % p == 0):
                primo = False

        if primo:
            cont = cont + 1
            if(cont == numero):
                break
        t = t + 1
        primo = True

        print(f"Numero primo --> {t}")
        return t

def mcd(a, b):
    while True:
        risultato = a % b
        if risultato == 0:
            break
        a, b = b, risultato
def mcm(a, b):
    return int((a * b)/mcd(a, b))
def trovaC(m):
    for i in range(2, m):
        if mcd(i, m) == 1:
            break
    return i
def trovaD(c, m):
    for i in range(1, m):
        if(i * c) % m == 1:
            break
    return i 
def algoritmo():
    p = 0
    q = 0

    while p == q:
        p = numeroPrimo()
        q = numeroPrimo()

    n = p * q
    print(f"N--> {n}")
    m = mcm(p-1, q-1) 
    print(f"M--> {m}")
    c = trovaC(m)
    print(f"C--> {c}")
    d = trovaD(c, m)
    print(f"D--> {d}")

    return d, c, n

def encode(message, c, n):
    return((message ** c) % n)
def decode(messagge, d, n):
    return((messagge ** d) % n)

d, c, n = algoritmo()

message = 75

print(f"Il messaggio da inviare è --> {message}")
sms_cod = encode(message, c, n)
print(f"Messaggio codificato --> {sms_cod}")
sms_enc = decode(sms_cod, d, n)
print("Il messaggio decodificato è --> {sms_enc}")