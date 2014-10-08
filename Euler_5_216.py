#
#
#
#

from Functions import IsPrime, RetFact

ctr = 0

for i in xrange(1,100001):
  a = 2 * (i * i) -1
  if IsPrime(a):
    print i, a
    #if IsPrime(i):
    #  print "!!!both prime",i
    ctr+=1


print "Number of Primes is", ctr
