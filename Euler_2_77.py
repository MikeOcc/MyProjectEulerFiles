#
#
# Euler Problem 77
#
#
from Functions import RofPrimes
from time import time

st = time()

primes = RofPrimes(2,100)
cutoff = 5000

# take a guess, the numbers increase geometrically, or exponentially, not sure which, but the # of ways is far fewer than the answer for 100 
max = 50
while 1:
  perms = [1] + [0] * max
  for i in primes:
    for j in range(i, max+1):
      #temp = perms[j]
      perms[j] += perms[j-i]
      #print i, j, temp,perms[j-i] , perms[j] 
  if perms[max] > cutoff: break
  max += 1;

print
print perms

print "Answer is", max
print "Process time is", time()-st
