#
#
# Euler 132
#
#

from Functions import RofPrimes
from time import time

st = time()
P = RofPrimes(11,10**6)

ctr = 0
tot = 0
for p in P:
  if pow(10,10**9,p) == 1:
    print p,
    tot +=p
    ctr +=1

  if ctr == 40: break
print
print
print "Sum of first 40 primes in R(10**9) is",tot
print "process time is", time()-st




