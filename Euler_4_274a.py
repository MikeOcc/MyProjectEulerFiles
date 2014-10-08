#
#
#  Euler Problem 274
#
#[]

from Functions import gcd, RofPrimes
from time import time

def isInt(a):

  return int(a)==a

def f(n,m):

  a = n/10
  x = a + (n-a*10)*m

  return x

#########################

st = time()
summ = 0
primes = RofPrimes(2,10**7)

for p in primes:
  for i in xrange(1,p):
    #n = 9*p
    x = f(9*p,i)
    x1=x/float(p)
    #print p, i, x1
    if isInt(x1):
      print p, i, x
      summ += i
      break
      

print
print "total is", summ
print "process time is",time()-st




