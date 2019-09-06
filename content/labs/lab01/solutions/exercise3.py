def isprime(N):
    count = 0;
    if not isinstance(N, int):
        return False
    if N <= 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            count = count + 1;
    if count == 0:
        return(True)
    else:
        return(False)
    
print(isprime(3.0), isprime("pavlos"), isprime(0), isprime(-1), isprime(1), isprime(2), isprime(93), isprime(97))    
myprimes = [j for j in range(1, 100) if isprime(j)]
print(myprimes)
