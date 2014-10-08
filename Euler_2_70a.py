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

  phi = 1

  for i in facts:
    phi *= (i-1)
    #phi /= i

  return phi


st = time()
rato = 0
minrat = 10
answer = 0

primes = RofPrimes(2200,2500)
primes2 = RofPrimes(3300,3600)

for a in primes2:
  for b in primes:
   n = a*b
   if n>10000000:continue

   factors = RetFact(n)
   phi = Phi(n,factors)

   set1 = sorted(list(str(n)))
   set2 = sorted(list(str(phi)))

   if set1 == set2: 
     rato = float(n)/float(phi)
     if rato<minrat:minrat = rato;answer = n
     print "!!!!!",n,":", phi,":",factors,":",rato
  #else:  print n,":",factors,":",phi


print
print "The minimum ratio of n/phi(n) is",minrat,"for n =",answer  
print
print "process time is ",time()-st
