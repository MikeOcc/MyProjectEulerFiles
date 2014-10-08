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
from Functions import RetFact,primes
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

F = FactorSieve(500000)
p = primes(20000000)
#print F
print time()-st
#exit()

summ=0
#x=20000000
#y=5000000
z=5000000
for x in xrange(20000000,20000000-100,-1):

  if x in p:
    summ += x
    print "p",x
    continue
 
  elif x%z==0:
    v=x/z

    if v in F:
      summ += sum(F[v])
      print "1)",x,z,v
    else:
      summ += sum(RetFact(v))
      print "2)",x,z,v
    z-=1
    continue
#  elif miller_rabin(x):

  else:
    summ += sum(RetFact(x))    
    print "3)",x,z
print "summ", summ
print "z", z

 
 
 
 
 