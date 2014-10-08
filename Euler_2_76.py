#
#  Euler Problem 76
#

from itertools import combinations

P = [0]*101

for i in xrange(1,101):
  P[i]=0  
  sgn = 1
  for k in xrange(1,101):
    f = k * (3*k-1)/2
    
