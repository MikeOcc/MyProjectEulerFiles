from Functions import RetFact

global sqr
sqr=[]

def M(n):
  amax=0
  amost=0
  for a in xrange(n/2,n):
    v = a**2%n
    #v = sqr[a]%n
    if v==a and v>=amax:
      amax = v
      amost = a
    
      #print n,a,v
    if amax==0:amost,amax=1,1
  return amost,amax

	
tot = 0

for k in xrange(11):
  sqr.append(k**2)


for j in xrange(2,21):
  m,max = M(j)
  tot += m
  if m>1:print "a:",j,RetFact(j),", n: ",max,RetFact(m),",",RetFact(m-1)
  #print

a2=[]

#for j in xrange(1,10**7):
#  a2.append(j*j)
  
print
print "total is ", tot
