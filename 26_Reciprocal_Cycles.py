import time
from math import sqrt
from math import floor
from math import log10

def products_of_2s_and_5s(limit):
    products = {2, 5}
    number_of_steps = floor(sqrt(limit))
    for step in range(number_of_steps):
        for item in products.copy():
            if item*2 < limit:
                products.add(item*2)
            if item*5 < limit:
                products.add(item*5)
    return products

def convert_fraction_to_decimal(numerator, denominator):
    denominator_number_of_digits = int(log10(denominator))+1
    dividend = numerator*10**denominator_number_of_digits
    divisor = denominator
    decimal = "0." + (denominator_number_of_digits-1)*"0"
    remainders = []
    max_number_of_digits = denominator # The period of m/n is at most n-1 digits long
    for digit_number in range(max_number_of_digits):
        digit = floor(dividend/divisor)
        #decimal = decimal + str(digit)
        remainder = dividend % divisor
        if remainder == 0:
            decimal = decimal + " [finite]"
            return decimal
            break 
        elif remainder in remainders:
            decimal = decimal + " [periodic]"
            return decimal
            break
        else:
            decimal = decimal + str(digit)
            dividend = remainder*10
            remainders.append(remainder)
            if digit_number == denominator:
                print("You made a mistake somewhere")

def find_length_recurring_cycle(numerator, denominator):
    denominator_number_of_digits = int(log10(denominator))+1
    dividend = numerator*10**denominator_number_of_digits
    divisor = denominator
    remainders = []
    period = []
    max_number_of_digits = denominator
    for digit_number in range(max_number_of_digits):
        digit = floor(dividend/divisor)
        remainder = dividend % divisor
        if remainder == 0: # decimal is finite
            return 0
            break
        elif remainder in remainders: # period found
            return len(period)
            break
        else: # period not yet found
            period.append(digit)
            dividend = remainder*10
            remainders.append(remainder)    
            
start = time.time()
max_length = 0
denominator_max_length = 0
for denominator in range(2, 1000):
    period_length = find_length_recurring_cycle(1, denominator)
    if period_length >= max_length:
        max_length = period_length
        denominator_max_length = denominator
print(denominator_max_length)   
end = time.time()
print(end - start)
