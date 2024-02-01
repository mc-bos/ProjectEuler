single_digit_primes = {'2', '3', '5', '7'}

number = '3797'
#for number in range(100, 3798):
#    if {str(number)[0], str(number)[-1]} <= single_digit_primes:

#left_to_right = set()
#right_to_left = set()
#for i in range(len(number)):
#    left_to_right.add(number[i:])
#    right_to_left.add(number[:i+1])
#print(left_to_right)
#print(right_to_left)

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

#for number in range (100, 3798):
#number = 3797
def is_truncatable_prime(number):
    if is_prime(number) == True:
        truncated = set()
        for i in range(len(str(number))):
            truncated.add(int(str(number)[i:])) # left to right
            truncated.add(int(str(number)[:i+1])) # right to left
        # print(truncated)
        for item in truncated:
            # print(item)
            # print(is_prime(item))
            if is_prime(item) == False:
                return False
                break
        return True
    return False

truncatable_primes = []
n = 10
while len(truncatable_primes) < 11:
    if is_truncatable_prime(n):
        truncatable_primes.append(n)
        print(truncatable_primes)
    n += 1

print(sum(truncatable_primes))

#print(is_truncatable_prime(3797)) # number is truncatable prime
#print(is_truncatable_prime(3798)) # number is not prime
#print(is_truncatable_prime(47)) # number is prime, but not truncatable prime
