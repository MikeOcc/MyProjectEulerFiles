###
#  
# Project Euler Problem 28: Find the sum of both diagonals in a 1001 by 1001 spiral
###

from math import *

#n = 500  # nth ring number, 0th Ring is sole digit 1
# S = 2*n+1 =>Spiral number  (n=2 => 3 x 3 Spiral, n=3 => 5 x 5, etc.)

#  2 line solution
S = 1001
#print sum(2*((2*i**2) - 3*(i-1)) for i in range(3,S+1,2)) +1

print "__________"

# One line solution
print "Sum of both diagonals in a 1001 by 1001 spiral *using squares* is", sum(2*((2*i**2) - 3*(i-1)) for i in range(3,1001+1,2)) +1

#test
#sum(23+29+32*n for n in range(0,5))+24

sum1 = 0
tempsum = 0

for j in range(1,500):
  tempsum = sum(23+29+32*n for n in range(0,j))+24
  
  #print tempsum
  sum1 += tempsum

print "__________"
print "sum of both diagonals in a 1001 by 1001 spiral with linear seq",sum1

#-------------------

print "__________"

#print sum(sum(32*n+52 for n in xrange(i))+24) for i in xrange(500))

print "sum of of both diagonals in a 1001 by 1001 spiral *shortest new way* =", sum(sum((32*n + 52) for n in xrange(i))+24 for i in xrange(500)) +1



