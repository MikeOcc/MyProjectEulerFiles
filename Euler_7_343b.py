from array import array

def factor1(N):
    N += 2
 
    factor_sieve = array('L', [0]) * N
    for i in xrange(2, N):
        if factor_sieve[i] == 0:
            for j in xrange(i,N,i):
                factor_sieve[j] = i
    return factor_sieve
 

def factor2(N):
    N+=2
    eqn_sieve = [k*k - k + 1 for k in xrange(N)]
    eqfactlist = [0] * N
    for k in xrange(1, N):
        num = eqn_sieve[k]
        if num > 1:   #  number still needs factoring
            j = k
            while j < N:
                while eqn_sieve[j] % num == 0:
                    eqn_sieve[j] /= num
                if eqfactlist[j] < num:
                    eqfactlist[j] = num
                j += num
    return eqfactlist


if __name__ == "__main__":

    from time import time
    st = time()
    MAX = 2 * 10**6
    facts1 = factor1(MAX)
    facts2 = factor2(MAX)

    for j in xrange(len(facts2)):
      print j,j*j-j+1,facts2[j]

    summ = 0
    for k in xrange(1, MAX+1):
        summ += max([facts1[k+1], facts2[k]]) - 1
 
    print "Answer is",summ
    print "Process time is", time()-st