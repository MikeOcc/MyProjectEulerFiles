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

def gm2(a,b,c):
  if g(a,b)==g(b,c)==g(a,c)==1:return True

def gm(a,b,c):
  if g(a,b)>1:return False
  if g(b,c)>1:return False
  if g(a,c)>1:return False
  return True
  
st=time()
N=120000
ctr=9
print "Calculating Factor Sieve for N=",N,"...",
f = FactorSieve(N)
print "done."
l = []
print "Generating list of semi-primes and powers...",
for i in xrange(32,N):
  s0=set(f[i])
  if (len(s0)==1 and len(f[i])>1) or (len(s0)==2 and len(f[i])>2):l.append(i)
print "done."
# for x in l:
  # print x,
# exit()

for c in l:
  for b in xrange(c-1,c/2,-1):
    s1=set(f[c])
    if len(s1)>2:continue
    a = c-b
    if a<b and gm(a,b,c) :
      #n = a*b*c
      #if (n-1)%2==0:print "odd",a,b,c,n
      #s1=set(f[c])
      s2=set(f[b])
      s3=set(f[a])
      #isPower=(len(s1)==1)		
      s = s1.union(s2.union(s3))
      #s = s.union(s3)
      v = reduce(mul,s)
      if v<c:
        #print a,b,c,":",s,s1,RetFact(c)
        ctr+=c
        #if not isPower:break
print "count is", ctr
print "time elapsed is", time()-st