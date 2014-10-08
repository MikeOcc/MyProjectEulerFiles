#
#
#  Euler Problem 341 test.
#
#
from mpmath import *

x = 1
incr = 1
incr2 =1
bump = 0.0
flipflop = True
def a(n):
  if n ==1:
    return n
  else:
    return (1 + a(n -a(a(n-1))))

 
#a=[1]
for i in xrange(1,10000):
  print a(i)
 