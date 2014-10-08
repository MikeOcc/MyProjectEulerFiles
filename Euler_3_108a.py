#
#
#
#  x + y = xy/n
#
#  1/x = 1/n - 1/y
#  
#
#
from Functions import RetFact, IsPrime
n = 1260 #500000000
maxx = 0
for n in xrange(10**8, 10**9):  #15000):
  if IsPrime(n):continue
  x = RetFact(n**2)
  s = set(x)
  facts = []
  for f in s:
    facts.append(x.count(f)+1)
  m=1
  for f in facts:
    m*=f
  m+=1
  m/=2

  if m>maxx:
    maxx=m
    print "!!!!!",n,":",m
  else:
    print n,":",m
  if maxx>4000000:print "Over 4 Mil!",n,m

print
print "# of solutions for",n, "is", maxx

     






