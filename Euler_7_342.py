#
#
#  Euler Problem 342
#
#
from Functions import RetFact
from time import time
from itertools import *
st = time()

'''
x=10**8
i=9*10**7
while i<x:
 i+=1
 print i,RetFact(i)
print "process time is", time()-st
exit()
'''   #  ]

ctr=0;maxx=0


def divisorGen(n):
    factors = list(RetFact(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return



for ii in range(576,577):
  z = []
  xx = ii **3 # i**3
  if xx%2==0:
    factors = RetFact(xx)
    #print "factors:",v
    lfactors = len(factors)
    for j in xrange(1,lfactors+1):
      zz =combinations(factors,j)   
      for zzz in zz:
        print zzz


  print sorted(z)
 
      

   
print 
#print ctr,maxx


