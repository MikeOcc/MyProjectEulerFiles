#
#
# Euler 231
#
#

from time import time

def facPrimeSum(n, o, LPF):
  z = 0
  for i in xrange(o, n+1): 
    j = i
    while (j > 1):
      p = LPF[j]
      z += p
      j /= p
  
  return z;

  
st=time()

N = 20000000
K = 15000000
summ = 0
        
LPF = [2]*(N + 1)

# for i in xrange(2, N+1,2):
  # LPF[i] = 2
  
for i in xrange(3, int(N**1)+1,2):
  if (LPF[i] == 2):
    LPF[i] = i
    if (i * i <=N):
      for j in xrange(i*i,N+1,i):
        if (LPF[j] == 2):
          LPF[j] = i

print time()-st

# for i in xrange(40):
  # print i, LPF[i]
# print
		   
v = facPrimeSum(N,K+1, LPF)
summ = v
print "total sum of prime factors from 15Mil to 20Mil Factorial ", v
v=facPrimeSum(N-K,0, LPF)
summ -= v
print "sum of prime factors up to 50Mil Factorial", v


print "sum of prime factors for 20000000C15000000 is", summ
print "time elapsed ", time()-st
