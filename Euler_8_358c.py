#
#
#  Euler 358
#
#
from Functions import RofPrimes,IsPrime
from decimal import Decimal
from time import time

st = time()

b = 10


def isrep(p):

 b,t,r,n=10,0,1,0

 for j in xrange(50):
   t+=1
   x = r * b
   d = int(x/p)
   r = x % p
   n = n * b + d

   if (t == p-1):
     return n 

   if r == 1:
     return -1
 return n
     


ctr=0
for i in xrange(7246,7299):

  p = int(str(i)+'09891')
  #print p

  if IsPrime(p):
     print "!",p, isrep(p)
     a = (p-1)/2*9
     rm1 = i%40
     rm2 = i%120
     if rm1 not in (1,3,9,13,27,31,37,39): #  and rm2==23:
       v = (10**20-1)/p
       print p, a, p%50,p%120, Decimal(1.0*10**19/p), 56789*p
       ctr+=1


print "count is", ctr
print "process time is", time()-st