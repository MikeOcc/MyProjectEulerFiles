#
#
# Euler 278
#
#

from time import time
from Functions import primes
from collections import defaultdict

def FactorSieve(n):
  
  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:

       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
           f[i].append(p)
       if f[p]==[]:f[p]=[p]
  return f



st=time()
#v(1+b2), v(1+c2) and v(b2+c2)

#F=FactorSieve(1250002)

def T(b,c):
  a2 = 1 + b*b
  b2 = 1 + c*c
  c2 = b*b + c*c
  #return (((4*a2*b2) - (a2 + b2 - c2)**2)**.5)/4.
  return (((4*a2*b2) - 4)**.5)/4.

n=10**6
summ = 0
for i in xrange(2,420,2):
  for j in xrange(i,1250000,2):
    A = T(i,j)
    if int(A)==A and A<=n:
      summ += int(A)
      #print i,j,int(A),F[i],F[j]
    if A>n:break

  
print "sum of funky triangles is ",summ
print "time elapsed ", time()-st
