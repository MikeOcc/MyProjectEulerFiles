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

  ns = str(n)
  l = len(ns)
  a = ns[:l-1]
  b = ns[-1]

  #print a, b
  x = int(a) + int(b)*m
  return x

'''
print 4407/113.
x=f(4407,34)
print x,x/113.
'''
st = time()
summ = 0
primes = RofPrimes(2,10**3)

for p in primes:
  for i in xrange(p,0,-1):
    n = 9*p
    x = f(n,i)
    n1,x1=n/float(p), x/float(p)
    if isInt(n1) and isInt(x1):
      #print p, i
      summ += i
      break
      

print
print "total is", summ
print "process time is",time()-st




