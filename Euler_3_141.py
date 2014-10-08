#
#
#  Euler Problem 141
#
#
from Functions import RetFact

def geo(l):

  l2=sorted(l)
  rat = l2[1]/float(l2[0])
  rat1 = l2[2]/float(l2[1])

  return rat==rat1


sqr = [i**2 for i in xrange(10**6) if (i%3==0 or i%5==0 or i%7==0)]
summ = 0
for n in sqr:
  for d in xrange(1,int(n**.5)):
    #if not (n%3==0 or n%5==0):continue
    q = n/d
    r = n%d
    if r==0: continue
    s = (d,q,r)
    L = list(s)
    
    if geo(L):
      print n, r, d, q, ":", d/float(r), RetFact(n) #sorted(L)
      summ += n
      break

print "answer is",summ
  
     





