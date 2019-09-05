N = 100;

# using loops and if statements
primes = [];
for j in range(2, N):
    count = 0;
    for i in range(2,j):
        if j % i == 0:
            count = count + 1;
    if count == 0:
        primes.append(j)
print(primes)
