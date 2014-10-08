#
#
#  Euler 73
#

from Functions import gcd,primes
from math import ceil
from time import time
from collections import defaultdict


def Factor(n):

  n += 1
  factors = defaultdict(list)

  for p in xrange(2, n):
     if p not in factors:

       for i in xrange(p, n, p):
         factors[i].append(p)
  
  return factors


#
# Start program by performing a factor sieve to use
# for gcd equiv. by taking set intersection of factors
#
st=time()
ctr = -2  # easy way to eliminate 1/2 and 1/3 boundaries

f=Factor(12000)
nullSet = set([])

for i in xrange(1,12001):

  if f[i]==[i]:
    ctr+=(i>>1)-(int(ceil(i/3.)))+1
  else:
    x=int(ceil(i/3.))
    iSet = set(f[i])
    for j in xrange(x,(i>>1)+1 ):
      if iSet.intersection(set(f[j]))==nullSet :
        ctr +=1

print "total is ", ctr
print "time elapsed is ", time()-st
