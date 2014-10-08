#
# Euler problem 62
#
from itertools import starmap
from operator import mul

def makeKey(n):
  return "".join(sorted(list(str(n))))

#sum(int(x) for x in list(str(12345)))

ydouble = []
ysingle = []
ylist = []
ytrip = []
for i in xrange(10,20000):

  y = i**3

  ctr=1
  ysum = makeKey(y)

#  if ysum == "00134677899" or ysum == "012334566789":print "!!!",ysum, i, y

  if ysum == "012334556789" :print "!!!",ysum, i, y


  if ysum not in ysingle:
     ysingle.append(ysum)
     ylist.append((ysum,i,y))
  elif ysum not in ydouble:
     ydouble.append(ysum)
   #  print "#$#", i,y,ysum
  else:
     #print "!", i,y, ysum
     ytrip.append((ysum,i,y))

print type(ytrip)
ytrip=list(ytrip)

ytrip= sorted(ytrip)

print
print
ytriplist = []
for xxx in ytrip:
    #print xxx
    ytriplist.append(xxx[0])

print 
print
ytriplist2=sorted(list(set(ytriplist)))
#for xxx in ytriplist2:
#  print xxx

print "*****************"

for xxx in ytriplist2:
  if ytriplist.count(xxx)>2:
    print xxx




