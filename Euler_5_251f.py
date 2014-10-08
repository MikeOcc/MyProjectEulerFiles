#
#  Euler Problem 251
#
#
#
from math import *
from time import time
from Functions import RetFact
from collections import defaultdict

# from functools import reduce
# from itertools import combinations
# from operator import mul

def FactorSieve(n):

  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:
  
       for i in xrange(p + p, n, p):
         #j, k = i, 1
         j = i
         while j % p == 0:
           j //= p
           #k *= p
           f[i].append(p)
       if p not in f:f[p]=[p]
  return f

st=time()

lim = 100000  # 10000

#F = FactorSieve(100**3)

a, b, c = 0,0,0

cnt = 0

for a in xrange(2,lim,3):

   x = (8*a*a*a + 15*a*a + 6*a - 1)
   if x%27==0: 

     x/=27    #   x = b*b*c
     y = RetFact(x)
     y.append(1)
     y=set(y)
     #print "!",a,y
     for z in y:
       b=z; c=int(x/(b**2))
      # print "!!",x,":",a,b,c
       if x==b*b*c:    
         if a+b+c<=1000:   #110000000:
           cnt+=1
           #print a,b,c

print "Number of Cardano Triplets <=",lim, "is", cnt
print "Process time is", time()-st
