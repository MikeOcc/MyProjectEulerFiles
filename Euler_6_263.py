from Functions import RofPrimes,IsPrime,divisors
from itertools import combinations
from time import time

def IsPractical(n):

  D = divisors(n)
  D.remove(n)

  l = len(D)

  slist = [1,n]

  for i in xrange(1,l+1):
    C = combinations(D,i)
    for c in C:

      s = sum(c)

      #print i, c, s

      if s<=n and s not in slist:
        slist.append(s)
      #elif s>n+6:break

  if len(slist) == n:
    print "*",n
    return True
  else:
    print "##" 
    return False

def PracticalSet(n):
  return IsPractical(n-8) and IsPractical(n-4) and IsPractical(n) and IsPractical(n+4) and IsPractical(n+8)


def IsSexyTrip(n):
  return IsPrime(n-9) and IsPrime(n-3) and IsPrime(n+3) and IsPrime(n+9)  

st = time()

'''

for n in xrange(5000,7000):
  IsSexy = IsSexyTrip(n)


  if IsSexy:
    print n,":",(n-9, n-3), (n-3,n+3), (n+3, n+9)
    IsPractSet = PracticalSet(n)
    if IsPractSet:
     print n,"!",n-8,n-4,n,n+4,n+8
'''

#PracticalSet(260)
IsPractical(224)

print "process time", time() - st






