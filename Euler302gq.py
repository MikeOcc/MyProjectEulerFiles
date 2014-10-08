

# Ideas:
# 1. Working on factorizations and not plain numbers
# 2. We will need factorizations of p-1 for each p prime
#    (to calculate factorization of phi(n))
# 3. If n is Strong Achilles numbers P^3 | n (for P - highest prime in factorization).
 
import fractions
 
def isqrt(n):
    xn = 1
    xn1 = (xn + n/xn)/2
    while abs(xn1 - xn) > 1:
        xn = xn1
        xn1 = (xn + n/xn)/2
    while xn1*xn1 > n:
        xn1 -= 1
    return xn1
 
def primeDiv(n):
    divs = []
    hi = isqrt(n)
    for p in primes:
        if p > hi: break
        if n%p == 0:
            exp = 2
            while n % (p**exp) == 0:
                exp += 1
            divs.append((p, exp-1))
            n /= (p**(exp-1))
 
    if n > 1:
        divs.append((n, 1))
 
    return divs
 
def GCDlist(nums):
    return reduce(fractions.gcd, nums)
 
factors = {}
 
def isSupAchill(min_prime_id, val, level):
    global result, fact_val, exp_list, factors
 
    print min_prime_id, val, level

    if exp_list[level] > 2 and GCDlist(exp_list[:level+1]) == 1:
 
        # Checking of phi(n)
        factors = {}
        for p,e in fact_val[:level+1]:
            factors[p] = e-1
 
            for pp, pe in preprimes[p]:
                if pp in factors:
                    factors[pp] += pe
                else:
                    factors[pp] = pe
 
        exponents = factors.values()
 
        if min(exponents) > 1 and GCDlist(exponents) == 1:
            result += 1
 
    level += 1
    for i in xrange(min_prime_id, primescnt):
        p = primes[i]
        next_val = val * (p ** 2)
        if next_val*p >= MAXN: break # Highest factor must be in 3rd power
        exp = 2
        while next_val < MAXN:
            fact_val[level] = (p, exp)
            exp_list[level] = exp
            isSupAchill(i + 1, next_val, level)
            next_val *= p
            exp += 1


################################################
from time import time
sttime = time()
 
MAXN = 10 ** 18
MAXP = 10 ** 6 + 1  # Ad. 3.
 
isprime = [i % 2 for i in xrange(MAXP + 1)]
isprime[1] = 0
isprime[2] = 1
 
primes = [2]
preprimes = {2: []}
 
hi = isqrt(MAXP)

for n in xrange(3, hi + 1, 2):
    if isprime[n] == 0: continue
    i = 3*n
    while i <= MAXP:
        isprime[i] = 0
        i += 2*n
 
print "Primes sieve calculated..."

print isprime
print len(isprime)

#exit()

for n in xrange(3, MAXP + 1, 2):
    if isprime[n]:
        primes.append(n)
        preprimes[n] = primeDiv(n-1)
 
primescnt = len(primes)
print "Precalculations finished (%d primes)" % (len(primes))
 
result = 0
 
fact_val = [0] * 10
exp_list = [0] * 10
 
for i in range(primescnt-1):
    p = primes[i]
    e = 2
    val = p ** 2
    tmp = primes[i+1] ** 3
    while val * tmp < MAXN: # There must be another bigger P^3
        fact_val[0] = (p, e)
        exp_list[0] = e
        isSupAchill(i+1, val, 0)
        val *= p
        e += 1
 
print result
print "Process time is",time() - sttime