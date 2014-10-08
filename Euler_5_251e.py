#
#  Euler Problem 251
#
#
#
from math import *
from time import time
st=time()

lim = 100

a, b, c = 0,0,0

cnt = 0

for a in xrange(2,lim,3):

  for b in xrange(1, lim - a):

    for c in xrange(1, lim - a - b):

        if (8*a*a*a + 15*a*a + 6*a - 1) == 27*b*b*c:
          if a+b+c<=110000000:
            cnt+=1
            print a,b,c



print "Number of Cardano Triplets <=",lim, "is", cnt
print "Process time is", time()-st
