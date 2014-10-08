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

def FactorSieve(m,n):
  
  n += 1
  f = defaultdict(list)
  summ=0
  for p in xrange(2, n):
     ss=0
     if p not in f:
       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
         #f[i].append(k)
           if p>=m:
             ss+=p
             # if p%4==0:
               # summ+=4 #f[i].append(p)
             # else:
             summ+=p
	 #if f[p]==[]:f[p]=[p]
     if ss==0 and p>=m:summ+=p
  return f,summ

st=time()

summ=1
x=20000000
y=5000000
z=5000000
for x in xrange(20000000,15000000,-1):
  
  vv = sum(RetFact(x))
  #print x,vv
  #print summ
  #z-=4

  
print summ
exit()

# x,s = FactorSieve(15*10**6,2*10**7)
# x,s2 = FactorSieve(1,5*10**6)
print s  
print s2
print s-s2
print len(x)
print time()-st
for i in x:
  print i, x[i]
  
  