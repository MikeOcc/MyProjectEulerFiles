#
# Problem 73
#
from math import *
from Functions import IsPrime,RofPrimes
from Functions import RetFact,gcd
from time import time

st = time()

mn = (1./3.)
mx = (1./2.)
print "1/3, 1/2", mn,mx
summ = 0
#factlist=[ ]

primes = RofPrimes(2,12001)
D = 12000
f=RetFact(D)

ctr=0
for d in range(5,D + 1):
   if d in primes:   #  IsPrime(d):
      strt = ceil(d*mn)
      endr = floor(d*mx)
      ctr += endr - strt + 1

   else:
      #facts = RetFact(d)
      strt = ceil(d*mn)
      endr = floor(d*mx)
      #print "Comp D:",d,strt,endr+1
      #g=RetFact(d)
      for i in xrange(int(strt),int(endr+1)):
         #a = RetFact(i)
         #if bool(set(a) & set(g))==False:
            #print i,":",a
         if gcd(i,d) ==1: 
            ctr+=1
            #print d,RetFact(i)
         #else:
         #   print d,RetFact(i)


print "Answer is",ctr
print "Process time is", time()-st
#short sol
#len(set([float(a)/b for a in xrange(1,12001) for b in range(a+1,12001) if float(a)/b > 1.0/3 if float(a)/b < .5 ]))


