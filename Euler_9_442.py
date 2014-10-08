#
#
#  Euler Problem 442
#
#

ll = [str(11**i) for i in xrange(1,17	)]
print ll
n=214
ctr=0
i=0
elfree=0
for i in xrange(600000):
  s = str(i)
  if ('11' in s or '121' in s or '1331' in s or '14641' in s or '161051' in s or '1771561' in s):
      #print i
    ctr+=1
    #break
  else:
    elfree+=1
    if elfree==500000:break
	
print "ctr ", ctr, elfree