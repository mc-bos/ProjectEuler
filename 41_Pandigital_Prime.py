from itertools import permutations

def is_prime(number):
    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    k = 5
    while k <= number**0.5:
        if number % k == 0 or number % (k+2) == 0:
            return False
        k = k + 6
    return True

input = '123456789'

pandigital = []
for index in range(2, len(input)):
    for permutation in permutations(input[:index], index):
        pandigital.append(int("".join(permutation)))

pandigital_primes = []
for item in pandigital:
    if is_prime(item):
        pandigital_primes.append(item)

print(max(pandigital_primes))
