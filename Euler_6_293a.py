#
#
# Euler Problem 293
#
#
from euler import miller_rabin
from time import time
st=time()
#p = [2,3,5,7,11,13,17,19,23]
d={}
 
for i in xrange(1,24):   #2
  for j in xrange(0,13):
    #if i==0 and j>0:break
    for k in xrange(0,9):
      if j==0 and k>0:break
      for m in xrange(0,5):       #7
        if (k==0 or j==0) and m>0:break
        for n in xrange(0,7):    #11
          if (k==0 or j==0 or m==0) and n>0:break
          for o in xrange(0,6):   #13
            if (k==0 or j==0 or m==0 or n==0) and o>0:break
            for p in xrange(0,4):  #17
              if (k==0 or j==0 or m==0 or n==0 or o==0) and p>0:break
              for q in xrange(0,3): #19
                if (k==0 or j==0 or m==0 or n==0 or o==0 or p==0) and q>0:break			  
                for r in xrange(0,1):  #23
                  if (k==0 or j==0 or m==0 or n==0 or o==0 or p==0 or q==0) and r>0:break                  
                  N = 2**i * 3**j * 5**k * 7**m * 11**n * 13**o * 17**p * 19** q * 23**r;N1=N+1
                  if N >= 1000000000:continue
                  while True:
                    N1 +=2
                    if miller_rabin(N1):
                       M = N1-N
                       #if M not in d:print i,j,k,m,n,o,p,q,r,":",N,M
                       d[M]=1
                       #print i,j,k,m,n,o,p,q,r,":",N,M
                       break
                       #print i,j,k,m,n,o,p,q,r,":",N
summ=0
for p in d:
  #print p
  summ+=p
print "sum of distinct pseudo-fortunate numbers is", summ		   
print "time elapsed is",time()-st