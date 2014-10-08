#
#
#  Problem 347
#
#



from Functions import RetFact
from time import time
st = time()
tot=0
sl = []
s=[]
print "Processing..."
for i in xrange(10**2,5,-1):

  N = i
  maxj = 0
  for j in xrange(i,N+1):
    f = RetFact(j)
    s= set(f)
    #print "s",s
    if len(s)==2:
      if s not in sl:
        #print "*"
        sl.append(s)
        tot += j 
        print s,j     
      #else:
      #  print "dupe"


print "total is", tot
print "process time is", time()-st
#print sorted(list(sl))

   