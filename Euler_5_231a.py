#
#
# Euler 231
#
#

from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul
from time import time
from Functions import RetFact
from euler import miller_rabin

def FactorSieve(n):

  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:

       for i in xrange(p + p, n, p):
         j = i
         while j % p == 0:
           j //= p
           #f[i].append(p)
           f[i]=[p]
           break
		   
     if p not in f: f[p]=[p]
  return f

st=time()

F = FactorSieve(50000000)
#print F
print time()-st
exit()

summ=0
x=20000000
y=5000000
z=5000000
for x in xrange(20000000,15000000,-1):
 
  if x%z==0:
    v=x/z
    z-=1
    summ += sum(RetFact(v))
    continue
  elif miller_rabin(x):
    summ += x
    continue
  else:
    summ += sum(RetFact(x))    
    
    

 
 
 
 
 
 
 
 
 