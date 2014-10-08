#
#  Euler 302
#
# []

from Functions import RofPrimes,RetFact,IsPrime
from itertools import combinations

maxp = 11
p = RofPrimes(2,11)

lim = 10**4

def tf(f):
  t=list(f)

  for f1 in f:
     zz = RetFact(f1-1)
     #print "zz",zz
     for zzz in zz:
       #print "zzz",zzz
       if zzz not in f:
         t.append(zzz)
  t = sorted(list(set(t)))
  return t

for x in combinations(p,2):
  sp = tf(x)
  
