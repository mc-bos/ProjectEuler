import time

# Finds the highest common factor of two numbers using the Euclidean Algorithm
def Highest_Common_Factor(number1, number2):
    a = max(number1, number2)
    b = min(number1, number2)
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
        # print("(" + str(a) + ", " + str(b) + ")")
    return(a)

def sort_key(fraction):
    return fraction[2]

# print(Highest_Common_Factor(48, 18))

start = time.time()
proper_fractions = []
for denominator in range(2, 9):
    numerator = (3*denominator-1)/7
    if Highest_Common_Factor(numerator, denominator) == 1:
        proper_fractions.append(
            (numerator, denominator, numerator/denominator))
end = time.time()
print(end - start)

start = time.time()
proper_fractions.sort(key=sort_key)
end = time.time()
print(end - start)
#print(proper_fractions)

start = time.time()
print(proper_fractions[-1])
end = time.time()
print(end - start)

print(Highest_Common_Factor(428570, 999999))
