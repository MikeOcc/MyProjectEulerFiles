#
#
#  Euler 214
#
#


  
from collections import defaultdict
# from functools import reduce
# from itertools import combinations
# from operator import mul
from time import time
from euler import miller_rabin

def Factor(n):

  n += 1
  f = defaultdict(list)
  t = range(n)

  for p in xrange(2, n):
     if p not in f:
       t[p] = p - 1
       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
         f[i].append(k)
         t[i] = t[i] * (p - 1) // p
  return f, t

st = time()

  
F,Phi=Factor(10000001)
  
#print len(Phi)

def chain(n):

  ctr=1
  while n > 1:
    n = Phi[n]
    ctr +=1
  return ctr

summ=0
for i in xrange(8900000,10000001):
  if miller_rabin(i):
    l = chain(i)
    if l == 25:
      print i,l,F[i]
      summ+=i
print "sum is", summ
print time()-st












