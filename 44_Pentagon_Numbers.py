from math import sqrt

def is_pentagonal(number):
    if (sqrt(24*number+1)+1) % 6 == 0:
        return True #sqrt(24*number+1)/6
    else:
        return False

pentagonals = []
for n in range(1, 100000):
    pentagonals.append(n*(3*n-1)/2)

for pentagonal_j in pentagonals:
    j = pentagonals.index(pentagonal_j)
    for pentagonal_k in pentagonals[j+1:]:
        sum = pentagonal_j + pentagonal_k
        difference = pentagonal_k - pentagonal_j
        if is_pentagonal(sum) and is_pentagonal(difference):
            print(difference)

#for k in range(1,100):
#    pentagonal_k = k*(3*k-1)/2 # k = 7, P7 = 70
#    pentagonal_sum = (k+1)*(3*(k+1)-1)/2 # P8 = 92
#    pentagonal_j = pentagonal_sum - pentagonal_k # 22
#    if is_pentagonal(pentagonal_j) != False:
#        if is_pentagonal(pentagonal_k - pentagonal_j):
#            j = is_pentagonal(pentagonal_j)
#            print(j)
#            print(k)
