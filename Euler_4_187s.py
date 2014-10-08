#
#
#  Euler Problem 187
#
#
from Functions import RofPrimes
from time import time
from bisect import bisect
from math import sqrt

st=time()

PRIMES=RofPrimes(2,10**8/2)


N=10**8
 
TOTAL=0
for x in range(bisect(PRIMES,sqrt(N))):
    p=PRIMES[x]
    z = bisect(PRIMES,N/p)-x
    print x,p,N/p,z,PRIMES[z-1]
    TOTAL+=z
print TOTAL
print "process time is",time()-st




