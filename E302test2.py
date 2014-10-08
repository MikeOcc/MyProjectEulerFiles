#
#
# Euler Problem 2_70
#

from Functions import IsPrime, RetFact,RofPrimes
from time import time

def Phi(n,facts):

  phi = n

  for i in facts:
    phi *= (i-1)
    phi /= i

  return phi

def Phi2(n,facts):

  facts=list(set(facts))
  phi = n

  for i in facts:
    phi *= (i-1)
    phi /= i

  return phi


st = time()
rato = 0
minrat = 10
answer = 0

#primes = RofPrimes(2200,2500)
#primes2 = RofPrimes(3300,3600)

for n in xrange(10**8,10**8-100,-1):
   x = RetFact(n)
   print n, ":",x


print
print "process time is ",time()-st
