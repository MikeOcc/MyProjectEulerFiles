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

for i in xrange(4,40):

  if IsPrime(i): continue
  #print "****"
  d = divisors(i)
  d.remove(1)
  d.remove(i)

  if i**.5 == int(i**.5):
    tmp = []
    for x in d:
       if x <= i**.5:
         tmp.append(x)
    for x in tmp:
      d.append(x)

  #print "!",d 
  for x in xrange(2,len(d)+1):
    f1 = combinations(d,x)
    for f in f1: 
      nover = 0
      nunder = 0
      prod = Prod(f)
      if prod == i:
        summ = sum(f)
        k = len(f) + prod - summ
        print i,f,prod, summ, len(f), k
        if k not in psnum:
           psnum[k]=i
        elif i < psnum[k]:
           print "%"
           psnum[k]=i
      elif prod > i:nover +=1
      elif prod < i:nunder +=1
      if nover>2 or nunder>6:break 
  
  d = RetFact(i)
  if len(set(d)) == 1:
    prod = Prod(d)
    summ = sum(d)
    k = len(d) + prod - summ
    print i,d,prod, summ, len(d), k
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
 
  if psnum[b] not in dupes:
    if b <= 12:
      print b,psnum[b]
      tot += psnum[b]
    dupes.append(psnum[b])

print "total is", tot
print "process time is", time()-st
