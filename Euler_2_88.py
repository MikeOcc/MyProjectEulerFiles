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

psnum = {}

for i in xrange(4,12500):

  if IsPrime(i): continue
  #print "****"
  d = divisors(i)
  d.remove(1)

  if i**.5 == int(i**.5):
    tmp = []
    for x in d:
       if x <= i**.5:
         tmp.append(x)
    for x in tmp:
      d.append(x)

  #print "!",d 
  for x in xrange(2,len(d)):
    f1 = combinations(d,x)
    for f in f1: 
  
      prod = Prod(f)
      if prod == i:
        summ = sum(f)
        k = len(f) + prod - summ
        #print i,prod, summ, len(f), k
        if k not in psnum:
           psnum[k]=i
        elif i < psnum[k]:
           print "%"
           psnum[k]=i
       
  
  d = RetFact(i)
  if len(set(d)) == 1:
    prod = Prod(d)
    summ = sum(d)
    k = len(d) + prod - summ
    #print i,prod, summ, len(d), k
    if k not in psnum:
      psnum[k]=i
    elif i < psnum[k]:
      #print "&"
      psnum[k]=i

print
#print psnum
dupes = []
tot = 0
for a,b in enumerate(psnum):
  #print b,psnum[b]
  if psnum[b] not in dupes:
    if b <= 12000:
      tot += psnum[b]
    dupes.append(psnum[b])

print "total is", tot
print "process time is", time()-st
