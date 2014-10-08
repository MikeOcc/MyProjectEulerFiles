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

stor=[]


for i in range(2,1001):
  if IsPrime(i):continue
  v = divisors(i)
  f0 = RetFact(i)
  f=f0
  v.pop(-1)
  v.pop(0)
  for x in v:
    if x not in f:
      f += [x]
  f = sorted(f)
  #print f
  

    
  k=0
  #print "*",len(f),f

  
  for j in range(2,len(f)+1):  
    #print i,"JJJJJJJJJJJ",j
    f1 = combinations(f,j)
    
    for a in f1:
      if a in stor:continue
      n = Prod(a)
      k = n - sum(a) + len(a)
      if k > 12000: continue
      #print "Z:",k,a
      #print a, k,n   
      stor += [a]
      if k in d:
        if n < d[k]:
	      #if f> 100:print k,d[k],n,i,f
	      #num_dec +=1
	      d[k]= n
	      #print k,i ":", f*i, ":",(f*i)-(f+i) ,f, i 
      else:
        d[k]=n
        #if i==60 and 5 in a:print k,i, ":",n,a 
        #if i==24 :print k,i, ":",n,a 	
summ = 0

print 
print d
print d[6]
print
print len(d)

stor = []

for a in d:
  z = d[a]
  if z in stor:continue
  summ += z 
  stor += [z]

print "total is", summ
#print "process time is", time()-st

#print d
#print d[758]
#print d[248]
print
#print "# of k's:", len(d)
#print "total is :", summ
#print "num_dec is :", num_dec