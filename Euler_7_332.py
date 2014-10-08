#
#  Euler Problem 85
#
#
from math import sqrt

S = 14**2

for a in xrange(1,S):
  for b in xrange(1,S):
     if S > (a**2 + b**2):
       c = int(round(sqrt(S - a**2 -b**2),0))
       if a**2 + b**2 + c**2 == S:
         print "vertices a,b,c:",a,b,c

 


