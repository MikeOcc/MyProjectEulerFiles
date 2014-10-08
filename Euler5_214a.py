#
#
#  Problem 215
#
#

from Functions import RetFact,RofPrimes
from array import array

def phi(n):

  f = list(set(RetFact(n)))
  num,div = 1,1
  for x in f:
    num *= x-1
    div *= x
  return n*num/div


def chain(m):
  ctr = 1
  while 1:
    ctr+=1
    m = phi(m)
    if m ==1:
      return ctr
    
     
def factor1(N):
    N += 2
 
    factor_sieve = [()] * N
    for i in xrange(2, N):
        if factor_sieve[i] == ():
            for j in xrange(i,N,i):
                z=factor_sieve[j]+eval(str(i)+",")
                factor_sieve[j] = z
    return factor_sieve
'''
x = RofPrimes(2,40000000)

summ = 0

for i in xrange(len(x),2,-1):
  
  n = x[i-1]
  l = chain(n)
  
  if l==25:
    print n, l
    summ+=n


print "answer is",summ
'''

x = factor1(40000000)

for i in xrange(100):
  print x[i]




