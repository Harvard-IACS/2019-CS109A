primes_lc = [j for j in range(2, N) if all(j % i != 0 for i in range(2, j))]

print(primes)
print(primes_lc)
