#
#
#  Euler 355
#
#
from Functions3 import gcd,GCD
from itertools import combinations
from Functions import RofPrimes,RetFact,IsPrime



def Sum(L):
  return sum(L)

def notcoprime(cp,Y):
  for yy in Y:
    if gcd(yy,cp)!=1:
      return yy
  return -1

MX=10
x= RofPrimes(2,MX)
print GCD(x)
print x
print Sum(x)
y = list(x)
#x = sorted(x,reverse = False)
for i in xrange(MX-1,0,-1):
  if i in y:continue
  z= notcoprime(i,x)
  print i,z
  if z > 0 and i>z:
    x.remove(z)
  else:
    x.append(i)


print sorted(x)
print Sum(x)



