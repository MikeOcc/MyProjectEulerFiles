
from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul

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

  
  
  
f,t = Factor(1000000)
f=0
#print t
tot = 0

z=t[510510]

for i,x in enumerate(t):
  tot +=z *x
  #print i,x
  
print "total", tot