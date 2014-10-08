#
#  Euler Problem 85
#
#
from Functions import RetFact,IsPrime,divisors
from itertools import combinations
from time import time
st=time()

def Prod(facts):
  
  result = 1
  for fs in facts:
    result *= fs
  return result

#psnum = {}

d={}



for f in range(2, 111):	
  for i in range(2, 24000/f + 1):



    k = f * i - (f + i) + 2
  
    if k>12000:break
  
    n = f*i
    if k in d:
      if n < d[k]:
	    #if f> 100:print k,d[k],n,i,f
	    #num_dec +=1
	    d[k]= n
	   #   print k, ":", f*i, ":",(f*i)-(f+i) ,f, i 
    else:
      d[k]=n
      #if f> 110:print k,d[k],n,i,f
	
num_dec = 0

for i in range(107, 12001):

  f = 107
  #f = RetFact(i)
  #d = divisors(i)
  #print i, d

  k = f * i - (f + i) + 2
  
  if k>12000:break
  
  n = f*i
  if k in d:
    if n < d[k]:
	  d[k]= n
	 # print k, ":", f*i, ":",(f*i)-(f+i) ,f, i 
  else:
    d[k]=n	
	
	
for i in range(2, 30):

  #f = RetFact(i)
  #d = divisors(i)
  #print i, d

  k = 2 ** i - (2 * i) + i
  if k>12000:break
  
  n = 2**i
  if k in d:
    if n < d[k]:
	  d[k]= n
  else:
    d[k]=n
  
  print k, ":", 2**i, ":",(2*i)-(2+i) ,2, i

  
for i in range(3, 30):

  #f = RetFact(i)
  #d = divisors(i)
  #print i, d

  k = 3 ** i - (3 * i) + i
  if k>12000:break
  
  n = 3**i
  if k in d:
    if n < d[k]:
	  d[k]= n
  else:
    d[k]=n
  
  print k, ":", 3**i, ":",(3*i)-(3+i) ,3, i  
  
summ = 0
for a in d:
  summ += d[a]  
#print "total is", tot
#print "process time is", time()-st

#print d
print d[758]
print d[248]
print
print "# of k's:", len(d)
print "total is :", summ
print "num_dec is :", num_dec