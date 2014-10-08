from itertools import combinations, permutations

from Functions import nCr
from math import factorial
from time import time

def subFactorial(n):
  summ = 0
  for x in xrange(n+1): summ += float(pow(-1,x))/factorial(x)
  return factorial(n) * summ
    
def R(n,m,k):
  return nCr(n,k)*subFactorial(m-k)
  
st =time() 
z = 0.0
fixed = nCr(25, 3)
fact100 = factorial(100)

for k in xrange(23):z += R(75,97,k) * fixed / fact100
 
print "Probability is ", z
print "time elapsed ", time()-st

# for m in xrange(1,7):
  # print R(8,m)
  
# print R(25,22)
 
# print R(25,3)/factorial(25)
# print
# for i in xrange(25,101):
  # for j in xrange(3,79):
    # if j> i:continue
    # z = R(i,j)/factorial(i)
    #print i,j,z
    # if z > .050 and z< .07:
    #if z< .01:
      # print i,j,z


# for m in xrange(1,10):
  # print m,subFactorial(m)


# N=7
# p = primes(N)

# n = factorial(N)
# l = [m for m in xrange(1,N+1)]

# perm = permutations(l)

# total_deranged=0
# for P in perm:
  # num_pos = 0
  # ctr = 1
  # for x in P:
    #print ctr,x
    #if ctr == x and x in p:
    # if ctr == x :
      
      # num_pos +=1
    # ctr+=1
  # if num_pos ==2:
    # total_deranged+=1
    # print P

# print "total number of partial derangements is ",total_deranged
# print "total # of permutations is ", n
# print
# print "percentage of partial derangements is ", float(total_deranged)/n

    
