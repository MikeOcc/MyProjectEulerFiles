#
# Euler 380
#
#

from Functions import RetFact,divisors

ctr = 0

for b in xrange(1,333334):

  ctr+=1
  b2=b**2
  f = divisors(b2)
  #f.remove(1)
  f.remove(b2)
  l = len(f)
  for i in xrange(l-1,1,-1):
    c=f[i]
    a = b2/c
    if a<=b<=c and a+c>b and max(a,c)-min(a,c)<b:
       print b, a, c
       ctr+=1
    else: continue

print ctr





