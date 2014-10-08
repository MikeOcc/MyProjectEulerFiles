#
#
#  Euler Problem 111
#
#

from Functions import IsPrime
from itertools import permutations


x = "3"
total = 0
primes = []

for j in range(10):  #(1,2,4,5,7,8):
  print "#############"
  noprimes = False
  y = str(j)
  for k in xrange(10):
    x = str(k)
    for i in xrange(10):
      z = y*i + x + (9-i)*y
      zzz = IsPrime(int(z))
      if zzz:
        print j,z
        total += int(z)
        primes.append(int(z))
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
      primes.append(int(z))

  if noprimes == False:
    print "No primes found for d = 0"





for l in (2,8):

  print "$$$$$$$$$$$$$"
  noprimes = False

  w = str(l)


  for j in xrange(1,10):
    y = str(j)

    for k in xrange(1,10):
      x = str(k)
      if j==l or k == l: continue
      for a in xrange(10):
        for b in xrange(10):
            if b<a: continue
            z = w*8
            z = z[:a]+ x + z[a:]
            z = z[:b]+ y + z[b:]
            
            zzz = IsPrime(int(z))
            
            if zzz:
              print l,":",j,k,":",z
              total += int(z)
              noprimes = True
              primes.append(int(z))

  if noprimes == False:
    print "No primes found for d =",w

print
print "total sum of primes is",total
print sum(list(set(primes)))
