#
#
#  Euler Problem 90
#
#

from itertools import combinations
from time import time

st = time()

sqrs=[(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]

def allsquares(d1,d2):

  for sq in sqrs:
    n = sq[0];m = sq[1]
    #print n,m
    if sq==(0,9) and ((0 in d1 and (9 in d2 or 6 in d2)) or (0 in d2 and (9 in d1 or 6 in d1))):continue
    if sq==(1,6) and ((1 in d1 and (9 in d2 or 6 in d2)) or (1 in d2 and (9 in d1 or 6 in d1))):continue
    if sq==(3,6) and ((3 in d1 and (9 in d2 or 6 in d2)) or (3 in d2 and (9 in d1 or 6 in d1))):continue
    if sq==(4,9) and ((4 in d1 and (9 in d2 or 6 in d2)) or (4 in d2 and (9 in d1 or 6 in d1))):continue
    if sq==(6,4) and ((4 in d1 and (9 in d2 or 6 in d2)) or (4 in d2 and (9 in d1 or 6 in d1))):continue

    if ((n not in d1) or (m not in d2)) and ((m not in d1) or (n not in d2)):
       return False
  return True 

nums=[0,1,2,3,4,5,6,7,8,9]
dielist=[]
dice1 = combinations(nums,6)
ctr = 0

for die in dice1:
  #print die
  dielist.append(die)
  ctr += 1

print
print "total # of different dies:" , ctr    #  should equal nCr(10,6) of course

print
ctr = 0
for a in xrange(210):
  for b in xrange(210):
    if a>b: continue
    #print dielist[a],dielist[b]
    if allsquares(dielist[a],dielist[b]):
      ctr+=1
      #print a,b
      #print ctr,")",dielist[a],dielist[b] 

print "number of die configurations is", ctr
print "process time is", time()-st
