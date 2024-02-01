from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pandigitals = list(permutations(digits))
# print(pandigitals)

#pandigital = (1, 4, 0, 6, 3, 5, 7, 2, 8, 9)
# if int(str(pandigital[7]) + str(pandigital[8]) + str(pandigital[9])) % 17 == 0:
#pandigitals = [(1, 4, 0, 6, 3, 5, 7, 2, 8, 9), (1, 4, 0, 6, 3, 7, 5, 2, 8, 9)]

sum = 0
prime = [2, 3, 5, 7, 11, 13, 17]
for pandigital in pandigitals:
    for index in range(7, 0, -1):
        substring = int(str(pandigital[index]) + str(pandigital[index+1]) + str(pandigital[index+2]))
        if substring % prime[index-1] != 0:
            break
        elif index == 1:
            pandigital_integer = int(''.join(str(digit) for digit in pandigital))
            sum = sum + pandigital_integer
print(sum)
