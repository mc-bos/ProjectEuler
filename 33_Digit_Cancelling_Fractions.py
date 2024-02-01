def is_Digit_cancelling_fraction(numerator, denominator):
    if numerator >= denominator:
        return 'Fraction is more than one in value'
    if '0' in str(denominator):
        return False
    first_digit_numerator = int(str(numerator)[0])
    second_digit_numerator = int(str(numerator)[1])
    first_digit_denominator = int(str(denominator)[0])
    second_digit_denominator = int(str(denominator)[1])
    if first_digit_numerator == first_digit_denominator:
        if second_digit_numerator/second_digit_denominator == numerator/denominator:
            return True
    if first_digit_numerator == second_digit_denominator:
        if second_digit_numerator/first_digit_denominator == numerator/denominator:
            return True 
    if second_digit_numerator == first_digit_denominator:
        if first_digit_numerator/second_digit_denominator == numerator/denominator:
            return True
    if second_digit_numerator == second_digit_denominator:
        if first_digit_numerator/first_digit_denominator == numerator/denominator:
            return True

product_numerators = 1
product_denominators = 1
for denominator in range(10, 100):
    for numerator in range(10, denominator):
        if is_Digit_cancelling_fraction(numerator, denominator) == True:
            print(str(numerator) + '/' + str(denominator))
            product_numerators = product_numerators*numerator
            product_denominators = product_denominators*denominator
print(str(product_numerators) + '/' + str(product_denominators))

# Figure out why it doesn't return True for the trivial fraction 11/44?
numerator = 11
denominator = 44
print(is_Digit_cancelling_fraction(numerator, denominator))
