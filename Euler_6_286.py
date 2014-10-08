#
#
#  Euler Problem 286
#
#
from itertools import combinations

q = 51.

P = []

for x in xrange(1,51):

   v = (1-x/q)
   P.append(v)
   #print v


print P

P1 = combinations(P,20)

for p in P1:

  print p








