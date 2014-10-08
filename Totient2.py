


from Functions import IsPrime,RofPrimes
from math import log,floor


def MaxPrime(n):

  for x in xrange(n,0,-1):
    if IsPrime(x): return x

  return x

N=100

mp = MaxPrime(100)
x = RofPrimes(2,mp)
print x
l = len(x)
#ml = floor(log(N)/log(

for i in xrange(0,l):
  ml = int(floor(log(N)/log(x[i])))
  for j in xrange(1,ml+1):
    print x[i]**j





