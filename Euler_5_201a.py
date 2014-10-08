#
# Euler 201 adjunct
#
#


from Functions import nCr
from itertools import combinations

S = sorted(set(i*i for i in xrange(1,101)))
#S = sorted(set(i*i for i in xrange(100,1,-1)), reverse=True)


summin = sum(S[:50])

summax =  sum(S[50:])

print summin, summax, summax - summin

dict8 = {}
dict9 = {}

sets = combinations(S,4) 

for g in sets:
  #print g
  sum1 = sum(g)

  try:
    dict8[sum1]+=1
  except KeyError:
    dict8[sum1]=1


cnt1 = 0
cnt2 = 0
#prev = 0
#sum2 = 0
snglist=[]
for b in dict8.iteritems():

  if b[1]==1:
    x=b[0]
    #sum2+=x
    print x  #, x-prev
    cnt1+=1
    snglist.append(x)
  else:
    cnt2+=1

print "number of singles is", cnt1
print "number of multiples is", cnt2

print
sets = combinations(S,4) 
for c in sets:

  sum1 = sum(c)
  #print "sum1",sum1
  if sum1 in snglist:
    dict9[sum1]=c

print
print "******************"
setlist=[]
for b in sorted(dict9.iteritems(), key=lambda (k,v):(k,v)):
  print b[0],b[1]
  for v in b[1]:
    setlist.append(v)



set3 = set(setlist)
print
print "#################"
print sorted(set3)



