#
#
# Euler Problem 404
#
#
from time import time
from Functions import gcd,gcdtwo
from euler import miller_rabin

def isPS(n):
  z = int(n**.5)
  return z**2==n

st=time()
N = 10**17
ctr=0
for x in xrange(1,2 * int(N**.5) + 1):
  for y in xrange(x/2 + 1, x):
    v = ((x**2+y**2)/5)
    if ((x**2+y**2)/5.)==v:
      if isPS(v): 
        if gcdtwo(x,y)==1:
          a=x*y/2
          #print x,y,a,":",v
          ctr+=N/a

print ctr	  
print time()-st