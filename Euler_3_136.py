#
#
#  Euler 135
#
from Functions import RofPrimes,IsPrime

N = 5*10**7
L = [0]*(N+1) 
summ = 0

#primes = RofPrimes(2,N)
    
for i in xrange(1,N+1):
  for j in xrange(int(i/3),N/2 + 1):

     n = (3 * j**2) + (2 * j*i) - (i**2)
     if n > 0:
        if n < N:  # and L[n]<4: (falsely assumed that once an array slot was high enough I could break
           L[n] = L[n] + 1
        else:
           break

for i in xrange(1, N+1):
   if L[i] == 1: summ +=1
 
print "Answer is",summ
'''
print
for i in xrange(len(L)):
  if L[i] == 1:
    print i, L[i], ":", i%2, i%3, i%4, i%5, IsPrime(i),IsPrime(i-2)
'''




