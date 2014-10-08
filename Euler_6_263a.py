from Functions import RofPrimes,IsPrime,divisors
from itertools import combinations
from bisect import bisect
from time import time


def InD(k,subD):

  #print k, subD

  l = len(subD)

  for i in xrange(2,l+1):
  #for i in xrange(l,1,-1):
    C = combinations(subD,i)
    for c in C:

      s = sum(c)
      #print "!",s, c
      if s == k:return True
  return False

def IsPractical(n):

  D = divisors(n)

  for k in xrange(2,n):
   if k in D:continue
   f = bisect(D,k)
   if not InD(k,D[:f]): 
     #print n,k
     return False
  #print "Yes"
  return True




def PracticalSet(n):
  return IsPractical(n-8) and IsPractical(n-4) and IsPractical(n) and IsPractical(n+4) and IsPractical(n+8)


def IsSexyTrip(n):
  return IsPrime(n-9) and IsPrime(n-3) and IsPrime(n+3) and IsPrime(n+9)  


st = time()


for n in xrange(10000,30000):
  IsSexy = IsSexyTrip(n)


  if IsSexy:
    print n,":",(n-9, n-3), (n-3,n+3), (n+3, n+9)
    IsPractSet = PracticalSet(n)
    if IsPractSet:
     print n,"!",n-8,n-4,n,n+4,n+8
'''

#PracticalSet(260)
IsPractical(5390)

'''

print "process time", time() - st




