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


def phi(n):

  f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div


N=1000000000L
ctr=0

for i in xrange(N-1000000,N):

   sq = phi(i)*i
   cbr = int(round(sq**(1./3.),0))

   if  cbr**3 ==sq:
     print "Hit!",i,i*i,sq,cbr,RetFact(i)
     ctr+=i

print "total for ",N,"is",ctr






