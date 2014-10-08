#
#  Euler problem 131
#
#

from Functions import RofPrimes

primes = RofPrimes(2,10**6)

ctr=0
for p in primes:

  for j in xrange(1,p*p):
    i = j**3
    x = i**3 + i**2*p

    cub = x**(1/3.)
    if int(round(cub,4))**3 ==x:
      print p, i, x, cub
      ctr+=1
      break



print "total is", ctr






