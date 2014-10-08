
from Functions import gcd, RetFact, divisors
from math import factorial
from Functions import primes

# p = primes(10**8)

# print len(p)

# exit()


for i in xrange( 7 , 8):

  n = factorial(i)
  
  div = divisors(n)
  t = 0
  sqrtn = int(n**.5)
  print div
  for j in div:
    #if j> sqrtn:break
    if gcd(j,n/j) == 1:
       f = RetFact(j)
       #if set(f)==set([2,3,5,7]):
       print i, n, len(f),f, j
       t += j**2        # + (n/j)**2
#  print "tot:",i,n,RetFact(t), t%1000000009
#  print "tot:",i,RetFact(i),n, t, t%1000000009,RetFact(t%1000000009)
#  print "tot:",i,n,RetFact(n), t,RetFact(t), t%1000000009
  print 