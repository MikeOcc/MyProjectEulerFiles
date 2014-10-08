def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # recurrence formula for length by amount1 and amount2 Tony Veijalainen 2010
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    amount1 = n-10
    amount2 = 6

    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
             ## can you make recurrence formula for whole reciprocal?
            sieve[i*i//2::i] = [False] * (amount1//amount2+1)
        amount1-=4*i+4
        amount2+=4

    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]



x = primes(1000000)

print x
