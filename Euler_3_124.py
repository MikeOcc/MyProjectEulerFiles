#
#
#  Euler 124
#
# []
#

ls  = []

from Functions import RetFact,RofPrimes

primes = RofPrimes(2,100001)

for n in xrange(1,100001):

  if n in primes:
    ls.append((n,n))
    continue

  x = list(set(RetFact(n)))
  tot=1
  for y in x:
    tot*=y
  ls.append((tot,n))


ls = sorted(ls)

print ls[10000], ls[9999]

print "done"





