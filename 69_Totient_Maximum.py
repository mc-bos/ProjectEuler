def sieve(limit):
    primes = []
    multiples = set()
    for number in range(2, limit+1):
        if number not in multiples:
            primes.append(number)
            for multiple in range(number*2, limit+1, number):
                multiples.add(multiple)
    return primes

limit = 1000000
primes = sieve(200)
index = 1
result = primes[0]
while result*primes[index] <= limit:
    result *= primes[index]
    index += 1
print(result)
    
