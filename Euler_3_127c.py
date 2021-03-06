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
  #if g(b,c)>1:return False
  #if g(a,c)>1:return False
  return True
  
st=time()
N=1000
ctr=0
print "Calculating Factor Sieve for N=",N,"...",
f = FactorSieve(N)
print "done."
l = [1]
p=primes(620)
l+=p		
print "Generating list of semi-primes and powers...",
for i in xrange(2,N):
  s0=set(f[i])
  if (len(s0)==1 and len(f[i])>1) or (len(s0)==2 and len(f[i])>2) or (len(s0)==3 and len(f[i])>3):l.append(i)
l = sorted(l)
print "done."
# for x in l:
  # print x,
# exit()

for c in l:
  for a in l:
    s1=set(f[c])
    #if len(s1)>2:continue
    #a = c-b
    if a>c/2:break
    b = c-a
    #if a>=b:continue
    if g(a,b)==1 :
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