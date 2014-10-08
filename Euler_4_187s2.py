from time import time

def find_primes(n):
    """ returns a list of prime numbers from 2 to < n """
    if n < 2: return []
    if n == 2: return [2]
    # do only odd numbers starting at 3
    s = range(3, n, 2)
    # n**0.5 may be slightly faster than math.sqrt(n)
    mroot = n ** 0.5
    half = len(s)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)//2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m = 2 * i + 3
    # make exception for 2
    return [2]+[x for x in s if x]
 
def num_small_enough(p, n, primes):
    count = 0
    largest_possible = n/p
    for prime in primes:
        if prime > largest_possible:
            return count
        count += 1
    return count
 
def solve(n):
    primes = find_primes(n/2)
    sq = n**.5
    p_under = [p for p in primes if p <= sq]
    p_over = [p for p in primes if p > sq]
 
    print 'Primes calculated'
    count = 0
    for prime in p_under:
        biggest = n/prime
        count += num_small_enough(prime,n,p_over)
 
    return count + (1+len(p_under))*len(p_under)/2

st = time()
print solve(10**8)
print "process time is", time()-st