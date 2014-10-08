#
#
#  Euler 358
#
#
from Functions import RofPrimes

def HasAll(n):

  nstr=str(n)
  for j in xrange(1,10):
    if str(j) not in nstr:return False
  return True

b = 10
p = 13


P = RofPrimes(7,100)
for p in P:

 t = 0
 r = 1
 n=0

 while 1:
   #print "t", t
   t += 1
   x = r*b
   d = int(x/p)
   r = x%p
   n = n*b + d

   if r != 1: continue
   if t == p-1: 
     print n; len(str(n))
     break