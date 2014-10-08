import math

cmax = 2 * 10 ** 9
pmax = int(math.sqrt(cmax))
step = 10 ** 7

primes = [False] * 2 + [True] * int(math.sqrt(cmax))
for p in range(2, int(math.sqrt(pmax)) + 1):
    if primes[p]:
        for x in range(2 * p, pmax, p):
            primes[x] = False

primes = [n for n,i in enumerate(primes) if i]



def practical(x):
    sigma = 1
    for p in primes:
        if p > sigma + 1:
            return False
        if p * p > x:
            break
        e = 0
        while not x % p:
            x //= p
            e += 1
        if e:
            sigma *= (p ** (e + 1) - 1) // (p - 1)
    return True

def sieve(nmin, nmax):
    pp = [True] * (nmax - nmin + 1)
    for p in primes:
        if p * p > nmax: break
        for a in range( -nmin % p, len(pp), p):
            pp[a] = False
    return [p + nmin for p,a in enumerate(pp) if a]

tot = 0
n = 0
a = 2 * 10 ** 8
while True:
    pp = sieve(a, a + step)
    for i in range(3,len(pp) - 2):
        if pp[i] % 10 == 7 and all(pp[i] == pp[i+k] + x for x,k in zip(range(6,-13,-6),range(-1,3))) and \
           all(practical(pp[i] + k + 3) for k in range(-8,9,4)):
            tot += pp[i] + 3
            print(pp[i] + 3)
            n += 1
            if n == 4:
                break
    a += step

print(tot)