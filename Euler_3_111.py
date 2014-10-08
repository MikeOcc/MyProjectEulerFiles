#
#
#  Euler Problem 111
#
#

from Functions import IsPrime
from itertools import permutations


x = "3"
total = 0

for j in (1,2,4,5,7,8):
  print "#############"
  noprimes = False
  y = str(j)
  for k in xrange(1,10):
    x = str(k)
    for i in xrange(10):
      z = x*i + y + (9-i)*x
      zzz = IsPrime(int(z))
      if zzz:
        print j,z
        total += int(z)
        noprimes = True
  if noprimes == False:
    print "No primes found for d =",j


print "@@@@@@@@@@@@@"
noprimes = False

for j in xrange(1,10):
  y = str(j)

  for k in xrange(1,10):
    x = str(k)  
    z = x + "00000000" + y

    zzz = IsPrime(int(z))

    if zzz:
      print j,z
      total += int(z)
      noprimes = True

  if noprimes == False:
    print "No primes found for d = 0"


print "$$$$$$$$$$$$$"
noprimes = False


for l in (3,6,9):
  w = str(l)

  for j in xrange(1,10):
    y = str(j)

    for k in xrange(1,10):
      x = str(k)  
      z = x + w*8 + y

      zzz = IsPrime(int(z))

      if zzz:
        print j,z
        total += int(z)
        noprimes = True

    if noprimes == False:
      print "No primes found for d =",w

print
print "total sum of primes is",total

