from math import sqrt

def quadratic(a, b, n):
    f = n**2 + a*n + b
    return f

def sieve(limit):
    primes = []
    multiples = set()
    for number in range(2, limit+1):
        if number not in multiples:
            primes.append(number)
            for multiple in range(number*2, limit+1, number):
                multiples.add(multiple)
    return primes

def is_prime(number):
    if number < 2:
        return False
    elif number > 2:
        for prime_divisor in sieve(int(sqrt(number))+1):
            if number % prime_divisor == 0:
                return False
    return True

max_n = 0
max_a = 0
max_b = 0
for a in sieve(1000): # f will yield largest amount of primes if a is also prime
    for b in sieve(1001): # for f(0) to be prime, b has to be prime
        n = 0
        while True:
            if is_prime(quadratic(a, b, n)):
                if n > max_n:
                    max_n = n
                    max_a = a
                    max_b = b
                n = n + 1
            else:
                break
        n = 0
        while True:
            if is_prime(quadratic(-a, b, n)):
                if n > max_n:
                    max_n = n
                    max_a = -a
                    max_b = b
                n = n + 1
            else:
                break
        n = 0
        while True:
            if is_prime(quadratic(a, -b, n)):
                if n > max_n:
                    max_n = n
                    max_a = a
                    max_b = b
                n = n + 1
            else:
                break
        while True:
            if is_prime(quadratic(-a, -b, n)):
                if n > max_n:
                    max_n = n
                    max_a = a
                    max_b = b
            else:
                break
product = max_a*max_b

print("n: " + str(max_n))
print("a: " + str(max_a))
print("b: " + str(max_b))
print("product: " + str(product))
#for n in range(0, max_n+1):
#    print(quadratic(max_a, max_b, n))
