#
# Euler 2 - 57
#
#  1 + 1/(2 + 1/(2 + 1/(2 + 1/2)))
#
#3/2  7/5 17/12  41/29  99/70
#
#
#   5/2, 2+2/5,12/
#
from divide import MyDivide
from time import time
from math import log10
st=time()
d1 = 2.5
n = 3
d = 2

ctr = 0
print n,d,0, float(n)/float(d)

for i in xrange(1,1001):

    ntemp = n
    dtemp = d
    n = n + 2 * d
    d = ntemp + d
    n = d + dtemp
  
    #diff = len(str(n))-len(str(d))
    if int(log10(n)) - int(log10(d)) > 0: ctr +=1
    #print n,d,diff #, float(n)/float(d)

print "The number of factors with length of numerator greater than divisor is", ctr
#print "The square root of two is %.20f" % (float(n)/float(d))
print "Process time is" , time()-st
   