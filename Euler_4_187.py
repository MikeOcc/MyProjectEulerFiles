#
#
#  Euler Problem 187
#
#

from Functions import IsPrime, RetFact, RofPrimes
from time import time

st = time()
#primes = RofPrimes(2,10**5)

ctr = 0 
max1,max2 = 1,1

for i in xrange(4,10**4):
  if IsPrime(i):continue
  #if i in primes:continue
  x = RetFact(i)
  if len( x ) ==2:
    print i, x
    if x[0]>max1:max1=x[0]
    if x[1]>max2:max2=x[1]
    ctr += 1


print "total is", ctr
print "max factors are", max1, max2

print "process time is",time()-st

