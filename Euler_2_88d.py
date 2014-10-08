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

#psnum = {}

d1={}

for a in range(1,3):
  for b in range(1,3 ):
    for c in range(1,3 ):
     for d in range(1,3 ):
       for e in range(1,3 ):
        for f in range(1,3):
          for g in range(1,3):
           for h in range(1,3):
             for i in range(1,3):
              for j in range(1,4):
                for k in range(1,4):
                 for l in range(1,4):
                   for m in range(1,6):
                    for n in range(1,50):
                      for o in range(2,110):
                        f=0
                        f=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
                        #print "g",g
                        #f=copy(g)
                        #g=(filter(lambda a: a != 1, g))
                        f.remove(0)
                        while 1 in f:
                          f.remove(1)
                        #print
                        #print f
                        
                        n = Prod(f)
                        
                        k = n - sum(f) + len(f)
  
                        if k>12000:break
                        if k in d1:
                          if n < d1[k]:
                            d1[k]= n
                        else:
                          d1[k]=n
                        #print k,n  
  
  #print k, ":", 2*i, ":",(2*i)-(2+i) ,2, i

print
stor=[]
summ = 0
for a in d1:
  z = d1[a]
  if z in stor:continue
  summ += z
  stor += [z]

#print "total is", summ

print d1
#print d1[18]
print
print "# of k's:", len(d1)
print "total is :", summ
print "process time is", time()-st