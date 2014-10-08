

from time import time
from math import sqrt


st = time()


for i in xrange(100000):
  x = sqrt(10.01)
  
st = time()

for i in xrange(100000):
  x = (10.01)**.5
  
print "first time is ", time()-st


  
print "second time is ", time()-st
st = time()
for i in xrange(100000):
  x = pow(10.01,.5)
  
  
print "third time is ", time()-st