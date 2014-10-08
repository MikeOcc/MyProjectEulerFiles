#
#
#  Euler Problem 386
#
#
from collections import defaultdict
from Functions import divisors,RetFact,primes
from collections import defaultdict
#,FactorSieve
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

st=time()



print "Factoring Integers..."
#f = FactorSieve(N)
print "Done"
# for i in f:
  # print f[i]

summ = 0

def canAdd(s,y):
  #canAdd=True
  for z in s:
    if y>z:
      if y/z==(1.0 * y)/z:
        return False
    else:
      if z/y==(1.0 * z)/y:
        return False
  return True

  
def cntpowers(x):

  z = RetFact(x)
  S = set(z)
  summ = 0
  for SS in S:
    summ += z.count(SS)
  return summ
  
N = 4*10**5	
p = primes(N)
X=5
summm=0	
Z=60
for i in xrange(Z,Z+1):
  if i in p:
    summm+=1
    continue
  d = divisors(i)
  D = cntpowers(i)
  D2=D/2

  print i,d,D,D2,RetFact(i)
  for x in d:
    q = cntpowers(x)
    if q == D2:
     summm +=1
     print "*",x,RetFact(x)
    #print "*",x,RetFact(x)
 #if D==X: print 
	
print summm
print "time elapsed", time()-st

