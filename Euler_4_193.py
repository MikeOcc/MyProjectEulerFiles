#
#
# Euler Problem 193
#
#
from Functions import RetFact, IsPrime, RofPrimes

def mobius(n):
    result, i = 1, 2
    while n >= i:
        if n % i == 0:
            n = n / i
            if n % i == 0:
                return 0
            result = -result
        i = i + 1
    return result


mx = 33554432
primes = RofPrimes(2,mx)
lim = 2**50

ctr = 0

print len(primes)
print

for i in primes:

  fact = i**2
  ctr += int(lim/fact) * mobius(i)


print ctr

