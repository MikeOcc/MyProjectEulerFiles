#
#
#
#  x + y = xy/n
#
#  1/x = 1/n - 1/y
#  
#
#
from Functions import RetFact, IsPrime,RofPrimes
n = 2768774904222066200260800 # 720720000/(72*5) #500000000
maxx = 0
lim = 4000000

x=RofPrimes(17,1000)
ctr = 1

while 1:
  
  #n*=x[ctr]
  #if IsPrime(n):
  #  n+=1
  #  continue

  x = RetFact(n)
  s = set(x)
  facts = []
  for f in s:
    facts.append(x.count(f)*2+1)
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
  if maxx>=lim:
     print "Over 4 Mil!",n,m
     print RetFact(n)
     print facts
     break
  n*= 1260*143
  ctr +=1


print
print "# of solutions for",n, "is", maxx

     






