#
#
#  Euler Problem 342
#
#
from Functions import RetFact,IsPrime,RofPrimes
from time import time
from itertools import *
from array import array

def factor3(N):
    N+=2
    eqn_sieve = [k*k for k in xrange(N)]
    print eqn_sieve
    print
    eqfactlist = [()] * N
    print "!!!",type(eqfactlist[2]),eqfactlist[2]
    primes=RofPrimes(2,N+1)
    for k in xrange(2, N):
        num = eqn_sieve[k]
        if num > 1:   #  number still needs factoring
            if IsPrime(k):
              j=k
            else:
              continue
            #j = primes[k]
            while j < N:

                while eqn_sieve[j] % j == 0:

                    eqn_sieve[j] /= j
 
                    z=eqfactlist[j]
   
                    z+=eval(str(j)+",")
                    eqfactlist[j]=z

                j += j
    return eqfactlist

def factor2(N):
    N+=2
    eqn_sieve = [k*k for k in xrange(N)]
    print eqn_sieve
    print
    eqfactlist = [()] * N
    print "!!!",type(eqfactlist[2]),eqfactlist[2]
    for k in xrange(1, N):
        num = eqn_sieve[k]
        if num > 1:   #  number still needs factoring
            j = k
            while j < N:
                while eqn_sieve[j] % num == 0:
                    eqn_sieve[j] /= num
                #if eqfactlist[j] < num:
                    z=eqfactlist[j]
                    #print type(z)
                    z+=eval(str(num)+",")
                    eqfactlist[j]=z

                j += num
    return eqfactlist



def factor1(N):
    N += 2
 
    factor_sieve = array('L', [0]) * N
    for i in xrange(2, N):
        if factor_sieve[i] == 0:
            for j in xrange(i,N,i):
                factor_sieve[j] = i
    return factor_sieve

def S2(N):
#
# Factors numbers up to N into prime factors
#
    from array import array

    #N = max_k + 2
 
    sieve1 =  [()]* N
    #print "!!!",len(sieve1)
    for i in xrange(2, N):

        if sieve1[i] == ():
            # i is prime
            for j in xrange(i,N,i):
                sieve1[j] += eval(str(i)+",") #i
        #print i,":",sieve1
        #print    
    return sieve1

def phi(n):

  f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div

def phi2(n,f):

  #f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div

###################################

st = time()

N=5*10**6  #1000000000L
summ=0


x=S2(N)   # x[

#print len(x)

for i in xrange(2,len(x)):
  y = x[i]
  Phi = phi2(i,y)
  Phisq = i* Phi 
  cub = Phisq**(1/3.)
  if int(round(cub,4))**3 == Phisq:
    print i,y, Phi,":",i*i, Phisq,cub
    summ +=i


print "Sum is",summ


# 2,8,10,12,30,32,40,48,60,108




