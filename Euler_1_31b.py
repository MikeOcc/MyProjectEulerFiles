#
# Euler 31
#
#
from itertools import *
from string import rstrip
from time import time

st = time()

#print list(product([200,100,50,20,10,5,2,1] , repeat = 200))


cur = [100, 50, 20, 10,  5,   2,   1]
fac = [  3,  5, 11, 21, 41, 101, 201]
nms = ['pound','50 pence', '20 pence', '10 pence', '5 pence', '2 pence', 'pence']

val = 200
ctr = 8
cntdown = 8


from itertools import chain, combinations
def all_subsets(ss):
  return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

summ = 0
tot = 200
"""
for PC in all_subsets(cur):
  l = len(PC)
  curmin = PC[l]
  maxloops = int(200/curmin)
  for i in xrange(l):
   for j in xrange(maxloops):
"""

def sumcoins(a,b,c,d,e,f,g):
  return a*cur[0]+b*cur[1]+c*cur[2]+d*cur[3]+e*cur[4]+f*cur[5]+g*cur[6]
ctr = 0
for a in xrange(fac[0]): 
  for b in xrange(fac[1]): 
    for c in xrange(fac[2]): 
      for d in xrange(fac[3]): 
         for e in xrange(fac[4]): 
           for f in xrange(fac[5]): 
             for g in xrange(fac[6]): 
                tot = sumcoins(a,b,c,d,e,f,g)
                if tot > 200: break
                if tot == 200:
                     #print (a,b,c,d,e,f,g),";",tot
                     ctr+=1
                     summ +=1
                     tmp = list((a,b,c,d,e,f,g))
                     z= str(ctr)+") "
                     for k in xrange(7):
                       if tmp[k]>0:
                         z += str(tmp[k])+" "+nms[k]+", "
                     print rstrip(z,", ")


print "total number of combinations is " , summ
print "process time is", time()-st

