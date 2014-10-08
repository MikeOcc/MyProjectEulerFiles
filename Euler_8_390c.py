#
#
# Euler 278
#
#

from time import time
from Functions import primes,RetFact
from collections import defaultdict
from math import sqrt

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
F=FactorSieve(1250)

def T(b,c):
  a2 = b*b +1
  b2 = c*c +1
  #c2 = b*b + c*c
  #return (((4*a2*b2) - (a2 + b2 - c2)**2)**.5)/4.
  #A4=(((4*a2*b2) - 4)**.5)
  A42 = (a2*b2) - 1
  #A = pow(A42,.5)/2
  #A = (A42**.5)/2
  A = sqrt(A42)/2
  return A

n=10**8
summ = 0
for i in xrange(2,22872,2):
  for j in xrange(i,50000000,2):
    A = T(i,j)
    if int(A)==A and A<=n:
      summ += int(A)
      # if j in F:
      #print i,j,int(A) #,F[i],F[j]
      # else:
        # print "! ",i,j,int(A)  #,F[i],RetFact(j) #,RetFact(A)
    if A>n:
      #print "overflow at", i,j
      break

  
print "sum of funky triangles is ",summ
print "time elapsed ", time()-st
