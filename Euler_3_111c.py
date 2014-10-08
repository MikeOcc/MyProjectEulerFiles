#
#
#  Euler Problem 111
#
#

from Functions import IsPrime
from time import time
st = time()
total = 0

# Calculate primes for d=0, trivial
for i in range(1,10):
  for j in [1,3,7,9]:
    x = i*10**9 + j
    if IsPrime(x):
      total += x
      #print x
 

#print "---------------------------"
#print

# Calculate all primes with d = 8, only 2 numbers qualify
for i in [2,8]:
  x0=i * 1111111111
  for j in range(0,10):
    for k in range(0,10):
      if k<=j: continue
      #if j==10 and k==0: continue
      a,b = 10**j,10**k
      for l in range(10):
        for m in range(10):
          x = x0 + (l-i)*a + (m-i)*b
          if x%2==0 or x%3==0 or x<10**9:continue
          if IsPrime(x):
            total += x
            #print "Q:",x,j,k,l,m,-i*10**j ,- i*10**k ,+ l *10**j ,+ m*10**k	 
	  	  
#print "---------------------------"
#print "time elapsed is", time()-st

# Calculate all primes with d = 9, 7 numbers qualify	  
for i in [1,3,4,5,6,7,9]:
  x0 = i* 1111111111
  for j in range(0,10):
    b=10**j
    for k in range(0,10):
      x = x0 + (k-i) * b
      if x%2==0:continue
      if IsPrime(x):
        total += x
        #print x    #,i,j,k,i* 1111111111 , 10**j , k * 10**j
	  
print "total is: ", total
print "time elapsed is", time()-st
