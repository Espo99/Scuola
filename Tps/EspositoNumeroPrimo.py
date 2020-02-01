#Esposito Christian 5AROB

prime_number_min_5 = [1,2,3,5,6]
def primeNumberMag6(n_prime_number):
    k = 7
    cnt_prime_number = 5
    isPrime = True
    while True:
        for p in range(2, k//2):
            if (k % p == 0):
                isPrime = False

        if isPrime:
            cnt_prime_number = cnt_prime_number+1
            if (cnt_prime_number == n_prime_number):
                break
        k = k+1
        isPrime = True
    
    print(f"Numero primo > {k}")

n_prime_number = int(input("Inserisci la posizione del numero primo: "))

if (n_prime_number > 5):
    primeNumberMag6(n_prime_number)
else:
    print(f"Numero primo > {prime_number_min_5[n_prime_number-1]}")