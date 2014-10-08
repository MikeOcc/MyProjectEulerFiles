#
#
# Euler 127
#
#

from collections import defaultdict
from operator import mul
from Functions import gcd as g, RetFact, primes
from euler import miller_rabin
from time import time

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

def gm(a,b,c):
  if g(a,b)==g(b,c)==g(a,c)==1:return True
  
st=time()
N=1000
p=primes(N)
ctr=0

f = FactorSieve(100)

for x in f:
  print x,f[x]
exit

for c in xrange(3,N):
  for b in xrange(c-1,c/3,-1): 
    a = c-b
    if a<b and gm(a,b,c) :
      n = a*b*c
      if c in p:
        s1=set([c])
      else:
        s1=set(RetFact(c))

      if b in p:
        s2=set([b])
      else:
        s2=set(RetFact(b))
		
      if a in p:
        s3=set([a])
      else:
        s3=set(RetFact(a))
      isPower=(len(s1)==1)		
      s = s1.union(s2)
      s = s.union(s3)
      v = reduce(mul,s)
      if v<c:
        #print a,b,c,":",s,":",v,1.0*b/c
        ctr+=c
        if not isPower:break
print "count is", ctr
print "time elapsed is", time()-st