#
#
#  Euler Problem 187
#
#

from Functions import IsPrime, RetFact, RofPrimes
from time import time

st = time()
primes1 = RofPrimes(2,(10**8/2))
primes2 = RofPrimes(2,int((10**8)**.5)+1)

ctr = 0 

print "!!", len(primes1) , len(primes2)

for a in primes2:
  for b in primes1:
    if b>=a:
      if a*b<10**8:
        ctr+=1
      else:
        break

#ctr = len(primes1) * len(primes2)
print
print "total is", ctr

print "process time is",time()-st

