#
#
# Euler 278
#
#

from time import time
from Functions import primes
st=time()
#v(1+b2), v(1+c2) and v(b2+c2)

def T(b,c):
  a2 = 1 + b*b
  b2 = 1 + c*c
  c2 = b*b + c*c
  #return (((4*a2*b2) - (a2 + b2 - c2)**2)**.5)/4.
  return (((4*a2*b2) - 4)**.5)/4.

n=10**10
summ = 0
for i in xrange(2,1600,2):
  for j in xrange(i,1750000,2):
    A = T(i,j)
    if int(A)==A and A<=n:
      summ += int(A)
      print i,j,int(A)

  
print "sum of funky triangles is ",summ
print "time elapsed ", time()-st
