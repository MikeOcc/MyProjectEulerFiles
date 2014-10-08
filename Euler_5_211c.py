#
#
#  Euler Problem 211
#
#
from Functions import divisors,RetFact,primes

from time import time

N = 64000000

st = 0


def pe(n):
    pool = [k * k + 1 for k in range(n)]
    pool[1] = 1

    for k in range(2, (n + 1) // 2):
        k2 = k * k
        for m in range(k * 2, n, k):
            #print "k,m:",k,m,k*2
            pool[m] += k2

    s = 0
    for i, m in enumerate(pool):

        #print i, m 
        if m == int(m**.5)**2:
           #print i, m 
           s += i
    return s

print(pe(N))
print "time elapsed is ", time() -st