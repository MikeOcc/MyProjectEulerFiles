#
#
#  Euler Problem 211
#
#
from Functions import RetFact
from itertools import combinations, product

def divisors(n):
    factors = RetFact(n)
    factors.append(1)
    fact=[]
    l = len(factors)
    for z in xrange(2,l+1):
      y = combinations(factors,z)
      
      for yy in y:
         yyy = list(yy)
         #print yyy
         s1 = 1
         for yyyy in yyy:
           s1*=yyyy
         fact.append(s1)
    fact.append(1)
    fact = sorted(list(set(fact)))
    #print fact
    return fact

def O2(n):

  x = divisors(n)

  ssum = sum(int(i)**2 for i in x)

  return ssum


summ = 0
for i in xrange(64000000):
   x = O2(i)
   y = x**.5
   if int(y) * int(y) == x:
     print i, x, y
     summ +=i

print "answer is", summ





