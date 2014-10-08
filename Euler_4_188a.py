#
# Problem 188
#
#

from time import time

def HyperExMod(a,b,c):
  z=1
  while b:
 
      z = pow(a,z,10**c) 
      b-=1

  return z
  
st = time()
print HyperExMod(1777,10,8)
print "time elapsed is", time()-st