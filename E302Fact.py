#
#  find primes for factors of (p-1)
#  where p is a prime
#

from Functions import RetFact,RofPrimes

primes = RofPrimes(2,1000)

for p in primes:

  print p,":", RetFact(p-1)