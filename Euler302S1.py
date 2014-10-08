#
#
#



from Functions import primes, RetFact,gcd
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

p = primes(int((10**18/4)**(1/3.)))
F = FactorSieve(p[-1])

c = len(p)

plist={}

for i in xrange(2,200):
  q = p[i]
  f = F[q-1]
  s = set(f)
  l = list(s)
  #if 2 in s:remove(2)
  fl=[]
  for z in l:
    fl.append( z)
  print i,q,fl,f

	