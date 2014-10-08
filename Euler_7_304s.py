from itertools import *
from math import sqrt, log
 
# generate primes
def sieve(max_n):
    L = (max_n + 1) / 2
    a = [ True ] * L
    for k in ifilter(lambda p: a[p], xrange(1, int(sqrt(max_n)) / 2 + 1)):
        p = k * 2 + 1
        for n in xrange(k * 3 + 1, L, p):
            a[n] = False
    return [ 2 ] + map(lambda k: k * 2 + 1,
                ifilter(lambda k: a[k], xrange(1, L)))
 
def partial_sieve(start, end):
    a = [ True ] * (end - start)
    for p in takewhile(lambda p: p * p < end, primes):
        k0 = (start + p - 1) / p * p - start
        for k in xrange(k0, end - start, p):
            a[k] = False
            if not any(a):
                return 0
    return (start + k for k in xrange(end - start) if a[k])
 
def gen_primes(start, n):
    upper_prime = int(sqrt(start + 2 * n * log(start)))
    global primes
    primes = sieve(upper_prime)
    L = 10 ** 5
    k = 0
    p = M
    while True:
        for k, p in izip(count(k + 1), partial_sieve(p + 1, p + L)):
            yield p
            if k == n:
                break
        if k == n:
            break
 
# calculate fib
def mul(A, B):
    def f(i, k):
        return sum(A[i][j] * B[j][k] for j in xrange(nb)) % D
 
    na = len(A)
    nb = len(B)
    mb = len(B[1])
    return [ [ f(i, k) for k in xrange(mb) ] for i in xrange(na) ]
 
def square(A):
    a, b, d = A[0][0], A[0][1], A[1][1]
    a_ = (a * a + b * b) % D
    b_ = (b * (a + d)) % D
    return [ [ a_, b_ ], [ b_, a_ + b_ ] ]
 
def pow2(A, e):
    if e == 0:
        return [ [ 1 if i == k else 0 for k in xrange(len(A)) ]
                                            for i in xrange(len(A)) ]
 
    B = pow2(A, e / 2)
    C = square(B)
    return C if e % 2 == 0 else mul(C, A)
 
 
M = 10 ** 14
N = 10 ** 5
D = 1234567891011
A = [ [ 0, 1 ], [ 1, 1] ]
s = 0
prev_p = 1
prev_B = [ [ 1, 0 ], [ 0, 1 ] ]
for p in gen_primes(M, N):
    prev_B = mul(prev_B, pow2(A, p - prev_p))
    prev_p = p
    s += prev_B[1][1]
print s % D