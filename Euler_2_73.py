#
# Problem 73
#
from math import *
from Functions import IsPrime
from Functions import RetFact

mn = (1./3.)
mx = (1./2.)
print "1/3, 1/2", mn,mx
summ = 0
factlist=[ ]

D = 12000

for d in range(1,D + 1):
   if IsPrime(d):
      strt = ceil(d*mn)
      endr = floor(d*mx)
      print "Prime D:",d,strt,endr+1
      for x in xrange(int(strt),int(endr+1)):
        print "  X:",x
        if  mn < float(x)/d < mx:
           factlist.append(float(x)/d)
           print "    X-Factor:",x,float(x)/d
   else:
      #facts = RetFact(d)
      strt = ceil(d*mn)
      endr = floor(d*mx)
      print "Comp D:",d,strt,endr+1
      for x in xrange(int(strt),int(endr+1)):
        if  mn < float(x)/d < mx:
           print "  X:",x
           if not (float(x)/d ) in factlist:
            factlist.append(float(x)/d)
            print "    X-Factor:",x,float(x)/d

print factlist
print
print len(factlist)


