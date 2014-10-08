#
#
#  Euler Problem 201
#
from Functions import nCr
from itertools import combinations

#print nCr(100,50)

S = sorted(set(i*i for i in xrange(1,101)))
#S = sorted(set(i*i for i in xrange(100,1,-1)), reverse=True)

print S
print
print

dict1 = {}

sets = combinations(S,50)

cnt = 0

for e in sets:
  cnt+=1
  summ = sum(e)
#  print cnt,summ #, e

  try:
    dict1[summ]+=1
  except KeyError:
    dict1[summ]=1

  
  if cnt == 1000000000:break

print
print "********************"
print 
cnt1 = 0
prev = 0
sum2 = 0
#for b in sorted(dict1.iteritems(), key=lambda (k,v):(k,v)):
for b in sorted(dict1.iteritems(), key=lambda (k,v):(k,v)):
  if b[1]==1:
    x=b[0]
    sum2+=x
    print x, x-prev
    cnt1+=1
    prev = x
print "number of singles is", cnt1
print "sum of singles is", sum2




