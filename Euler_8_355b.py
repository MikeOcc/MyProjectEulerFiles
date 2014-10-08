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

from math import log
print notcoprime(6, [5, 7, 9, 8]),"!"
MX=20
x= RofPrimes(2,MX)
y=list(x)
tmp=[]
tmpr=[]
for y1 in x:
  z = log(MX)/log(y1)
  z1 = y1**int(z)
  tmp.append(z1)
  tmpr.append(y1)
  


print x
print tmp
for z in tmp:
  x.append(z)
for z in tmpr:
  x.remove(z)
x = sorted(x)
x.append(1)
print x
print Sum(x)


#x2 = sorted(x,reverse = True)

y = sorted(y,reverse=True)
#y=[7,5,2]
for z in y:
  #if z>=MX/2:break
  p = 0
  nprev,zprev,Oprev=0,0,0
  makechange = False
  while 1:
    p+=1
    v = z**p
    if v> MX:break
    for zz in x:
      New = v * zz
      if New >= MX:break
      Old1 = notcoprime(v,x)
      #print v,zz,New, Old1,":",v*zz,Old1+zz
      Prev = Old1 + zz
      print New>Prev
      if New > Prev:
        makechange = True
        if New>nprev:
           nprev=New
           zprev=zz
           Oprev=Old1
  if makechange == True:
    x.remove(Oprev)
    x.remove(zprev)
    x.append(nprev)

#x.append(1)
print sorted(x)
print Sum(x)
exit()
    




 
x.append(1)

print tmp
print sorted(x)
print Sum(x)



