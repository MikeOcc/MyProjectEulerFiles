#
#
#  Euler Problem 129
#

from Functions import gcd,RetFact,IsPrime
from Euler import miller_rabin

def repunit(n):
  return 10**n/9

  
#print repunit(17)

def A0(n):
  
  for k in xrange(2,17):
    
    x = repunit(k)
    if miller_rabin(x):continue
    f = RetFact(x)
    if n in f:
      return k
  return 0

def A(n,d):

  for c in d:
   if n in d[c]:
     return c
  return 0 
  
d={}
for k in xrange(2,21):
  x = repunit(k)
  if miller_rabin(x):
    d[k]=[x]  
    continue 
  f = RetFact(x)
  d[k]=f
  
print d
print  
  
for n in xrange(3, 20):
  if gcd(n,10) != 1: continue
  print n,
  print A(n,d)
  
# 11111111111111111  11111111111111111
# for i in xrange(10**6,10**6+10*3):
  #print i, gcd(i,10)
  # r = repunit(i)
  # for j in xrange(2,100):
   # n = r/float(j)
   # if gcd(n,10)!=1: continue
   # if n==int(n):
      # print i, r, n
      # break




