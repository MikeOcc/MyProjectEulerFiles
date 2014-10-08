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

def G(n):
  
  mp.dps=100
  n = mpf(n)
  two = mpf(2)
  one = mpf(1)
  #x = int(round(phi**(2-phi)*(n**(phi-1)),0))
  x = int(round(power(phi,(two-phi))*power(n,(phi-one)),0))
  return x

 
#a=[1]
summ=0
#
#print G(1000000-1)

for i in xrange(1,1000):
  x= G(i)    # a(i)
  print x
  summ += G(i**3)

print "sum is",summ