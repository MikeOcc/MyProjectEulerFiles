#
#  Euler Problem 85
#
#
from Functions import RetFact,IsPrime,divisors
from itertools import combinations
from time import time
from copy import copy
st=time()

def Prod(facts):
  
  result = 1
  for fs in facts:
    result *= fs
  return result
  
l=[]
d={}
  
for i in range(2,1000): 
  
  l=l+[i]
  f=copy(l)
  for j in range(1,14):

    f+=[2]
    #print f

    n = Prod(f)
    k = n - sum(f) + len(f)
    if k > 12000: continue
      # #print a, k,n   
      # #stor += [a]
    #print "k!",k,n,":",i,j
    if k in d:
      if n < d[k]:
      # #if f> 100:print k,d[k],n,i,f
      # #num_dec +=1
        d[k]= n
      # #print k,i ":", f*i, ":",(f*i)-(f+i) ,f, i 
    else:
      d[k]=n
	  
print
print d

print len(d)