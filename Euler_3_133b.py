#
#
#  Euler Problem 133
#
#
from Functions import RofPrimes
 
q = pow(10, 20)
summ = 3
x=RofPrimes(2,100000)

for p in x:
  if pow(10, q, p) != 1: summ += p
 
print
print "The Sum of Prime Never Factors is",summ





