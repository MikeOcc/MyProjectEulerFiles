#
#
#  various prime sieves and factor sieves
#

def S1(N):
#
# Determine largest prime factor
#
    from array import array

    #N = max_k + 2
 
    sieve1 = array('L', [0]) * N
    for i in xrange(2, N):

        if sieve1[i] == 0:
            # i is prime
            for j in xrange(i,N,i):
                sieve1[j] = i
        print i,":",sieve1
        print    
    return sieve1


def S2(N):
#
# Factors numbers up to N into prime factors
#
    from array import array

    #N = max_k + 2
 
    sieve1 =  [()]* N
    print "!!!",len(sieve1)
    for i in xrange(2, N):

        if sieve1[i] == ():
            # i is prime
            for j in xrange(i,N,i):
                sieve1[j] += eval(str(i)+",") #i
        print i,":",sieve1
        print    
    return sieve1


def FEq(N):
#
#  Factor an equation
#

    from array import array

    sieve2 = [k*k - k + 1 for k in xrange(N)]
    table2 = [0] * N
    for k in xrange(1, N):
        v2 = sieve2[k]
        if v2 > 1:
            # v2 needs factoring/primality test
 
            j = k
            while j < N:
            # for j in xrange(k, N, v2):
            # Check to see if v2 is a prime factor
                while sieve2[j] % v2 == 0:
                    sieve2[j] /= v2
                # check to see if new factor is larger
                #if table2[j] < v2:
                    table2[j] = v2
                #else:
                # test not needed since v2 constantly increases

                j += v2
            '''
            j = (1-k) % v2
            while j < N:
                print k,j,":",
            # for j in xrange((1-k) % v2, N, v2):
                while sieve2[j] % v2 == 0:
                    print "!!!",j,k
                    sieve2[j] /= v2
                if table2[j] < v2:
                    print "&&"
                    table2[j] = v2
                j += v2
            '''
    print sieve2
    print
    return table2

########

if __name__=="__main__":
  
  x = S2(30)   #S1(30)

  print "!!!!!!",x

  summ=0
  for i in xrange(30):
    print i,x[i]      #i,i*i - i + 1, x[i]
    #summ+=x[i][0]

  print "summ",summ


