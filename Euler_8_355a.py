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


print notcoprime(6, [5, 7, 9, 8]),"!"
MX=30
x= RofPrimes(2,MX)
print GCD(x)
print x
print Sum(x)
y = list(x)
tmp=[]
for i in xrange(MX,0,-1):
  if IsPrime(i):continue
  if i in tmp:continue
  if notcoprime(i,x)==-1:continue
  #print "!",i,x
  s = set(RetFact(i))
  isfactored = False
  for v in s:
    if v in tmp:isfactored = True;break
  if isfactored:continue
  if len(s) < 3:
    
    x.append(i)
    for z in s:
     if z in x:
       x.remove(z)
       tmp.append(z) 
x.append(1)

print tmp
print sorted(x)
print Sum(x)



