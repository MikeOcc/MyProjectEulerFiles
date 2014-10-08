#
#
#
#
#


from itertools import combinations
from euler import miller_rabin
from Functions import gcd

def gcd2(l):
  bzzz = True
  for z in xrange(len(l)):
    for y in xrange(len(l)):
      if z==y:continue
      if gcd(l[z],l[y])>1:
        bzzz = False
        break
  return bzzz
 
d={}
l=[]
for i in xrange(0,10):
  for j in xrange(0,10):
    if i==j==0:continue

    x = 2**i*3**j
    #print x
    if x<101:
      l.append(x)
	  
l = sorted(l)
print l

for k in xrange(2,6):
  c = combinations(l,k)

  for f in c:
    if gcd2(f):
      p = sum(f)

      if p>100:continue
      print k,f,p
      if miller_rabin(p):
        #print "prime ",f[0],f[1], p
        if p not in d :
          d[p]=1
        else:
          d[p]=d[p]+1
	  
summ = 0
for p in d:
  if d[p]==1:summ += p;print p
print summ

print
print d
#print sorted(d)