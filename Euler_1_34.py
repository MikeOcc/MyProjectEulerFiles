#Problem 34
#03 January 2003
#
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the #factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#
from time import time
from math import factorial
starttime=time()
sumunus = 0
ctr=0

for i in range(0,6):
  for j in range(0,10):
    for k in range(0,10):
      for l in range(0,10):
        for m in range(0,10):
          if i==0 and j==0 and k==0 and l==0:
            u=int(str(m))
            v=factorial(m)     
          elif i==0 and j==0 and k==0:
            u=int(str(l)+str(m))
            v=factorial(l)+factorial(m)       
          elif i==0 and j==0:
            u=int(str(k)+str(l)+str(m))
            v=factorial(k)+factorial(l)+factorial(m)
          elif i==0:
            u=int(str(j)+str(k)+str(l)+str(m))
            v=factorial(j)+factorial(k)+factorial(l)+factorial(m)
          else:
            u=int(str(i)+str(j)+str(k)+str(l)+str(m))
            v=factorial(i)+factorial(j)+factorial(k)+factorial(l)+factorial(m)
          w=""
          if u==v and (u!=1) and (u!=2): 
            w="!!!!!!!!"
            ctr+=1
            sumunus+=v
            print u,") ",v,w


print "# of hits is", ctr
print "The sum of the interesting numbers is",sumunus
print "Processing time is", time()-starttime