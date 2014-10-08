#
# Euler 2 - 57
#
#  1 + 1/(2 + 1/(2 + 1/(2 + 1/2)))
#
#3/2  7/5 17/12  41/29  99/70
#

from divide import MyDivide

d1 = (2+ .5)

for i in xrange(19):

   
   #d1 = 2 + 1/d1
   d1 = 2 + float(MyDivide(1,d1,20))
   #d1 = float(MyDivide(1,d1,20))
   #print i*2 + 5
   print "%.30f" % (d1)


print "%.30f" % (d1 - 1.0)
   