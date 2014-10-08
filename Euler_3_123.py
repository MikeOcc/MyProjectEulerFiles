#
#
#  Euler Problem 123
#
#
from Functions import RofPrimes
from time import time
st = time()

x=RofPrimes(2,10**7)

n = 15000  #7037
while 1:
  n+=1
  y=x[n-1]
  z=((y-1)**n + (y+1)**n)%(y*y)
  if z > 10**10:
    print "n found!", n
    print "value z", z
    break

print "process time", time()-st