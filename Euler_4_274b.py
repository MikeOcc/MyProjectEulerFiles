#
#
#  Euler Problem 274
#
#[]

from Functions import RofPrimes
from time import time

#########################

st = time()
summ = 0
primes = RofPrimes(3,10**7)

for p in primes:

  m = pow(10,p-2,p)
  summ += m

print
print "total is", summ
print "process time is",time()-st




