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
  p = pr[i]
  for j in xrange(i+1,l-1):
    q = pr[j]
    pq = p*q
    peasnqueues = 2*pq - p - q
    for k in xrange(j+1,l):
     summ +=  pr[k]*(peasnqueues) -pq 
 
print "sum of f(a,b,c) is ", summ
print "time elapsed ", time()-st
