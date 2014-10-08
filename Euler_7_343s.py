from array import array

def p343(max_k = 10**6*2):
    N = max_k + 2
 
    sieve1 = array('L', [0]) * N
    for i in xrange(2, N):
        if sieve1[i] == 0:
            # i is prime
            for j in xrange(i,N,i):
                sieve1[j] = i
 
    sieve2 = [k*k - k + 1 for k in xrange(N)]
    table2 = [0] * N
    for k in xrange(1, N):
        v2 = sieve2[k]
        if v2 > 1:
            # v2 is prime
 
            j = k
            while j < N:
            # for j in xrange(k, N, v2):
                while sieve2[j] % v2 == 0:
                    sieve2[j] /= v2
                if table2[j] < v2:
                    table2[j] = v2
                j += v2

            j = (1-k) % v2
            while j < N:
            # for j in xrange((1-k) % v2, N, v2):
                while sieve2[j] % v2 == 0:
                    sieve2[j] /= v2
                if table2[j] < v2:
                    table2[j] = v2
                j += v2

    res = 0
    for k in xrange(1, max_k+1):
        res += max([sieve1[k+1], table2[k]]) - 1
 
    return res

from time import time
st=time()

print p343(10**6*2)
print "process time is",time()-st