from Functions import RofPrimes,IsPrime,divisors,RetFact
from itertools import combinations
from bisect import bisect
from time import time
from math import log


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

  if n%2 != 0: return False
  
  #D = divisors(n)
  #if sum(D) == n*2: return True
  
  lg = log(n)/log(2)
  if lg == int(lg): return True
  
  F = RetFact(n)
  S = sorted(list(set(F)))
  
  for k in range(1,len(S)):
    a = S[k]
    f = S[:k]
    v = 1
    for fn in f:
      v*= fn**F.count(fn)
    w = sum(divisors(v)) + 1
    if a > w:
      print a, w,n,S  
      return False
  
  print "Yes",n
  return True


def PracticalSet(n):
  return IsPractical(n-8) and IsPractical(n-4) and IsPractical(n) and IsPractical(n+4) and IsPractical(n+8)


def IsSexyTrip(Ps):

  if Ps[1]-Ps[0] == 6 and Ps[2]-Ps[1] == 6 and Ps[3]-Ps[2] == 6:
      return True
  return False


def IsSexyTrip2(Ps):

  return IsPrime(i) and not IsPrime(i+3) and IsPrime(i+6) and not IsPrime(i+9) and IsPrime(i+12)

st = time()

#pl = len(P)

P0 = 210000001

tot = 0

for i in xrange(281935001,282000000,10):

  #IsSexy = IsSexyTrip(P[i:i+4])

  IsSexy = IsSexyTrip2(i)

  if IsSexy:
    #n = P[i] + 9
    n = i + 9
    print n,":",(n-9, n-3), (n-3,n+3), (n+3, n+9)
    IsPractSet = PracticalSet(n)
    if IsPractSet:
      print n,"engineers' paradise!",n-8,n-4,n,n+4,n+8
      tot += i

'''

#PracticalSet(260)
print IsPractical(128)

'''

print "process time", time() - st




