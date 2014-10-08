#
#
# Euler 278
#
#

from time import time
from Functions import primes

st=time()
N = 5000
summ = 0
pr=primes(N)
l = len(pr)

for i in xrange(l-2):
  for j in xrange(i+1,l-1):
   for k in xrange(j+1,l):
     p,q,r = pr[i],pr[j],pr[k]
     v = 2*p*q*r -p*q - p*r - q*r
     summ += v
 
print "sum of f(a,b,c) is ", summ
print "time elapsed ", time()-st
