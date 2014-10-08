#
#  Euler problem 65
#
#
from string import *
from math import e
from time import time
st = time()

elist = [2,1]
ctr=1
for i in xrange(1,99):
     if i%3 == 1:
       elist.append(2*ctr)
       ctr+=1
     else:
       elist.append(1)


print "len",len(elist)
print 
print elist
print

"""
estring = "("
for i in xrange(50):  #  len(elist)):
  estring += str(elist[i])+"+ 1./("

estring = estring.rstrip("/(")
estring = estring + 50 * ")"


eb = elist[0]
for i in xrange(1,5):
  ee = 1./(1 + 1./elist[i])
  print ee,
"""

print
#  Using the Babylonian Method
hn2 = 0
hn1 = 1
kn2 = 1
kn1 = 0
hn,kn=[],[]


for i in xrange(0,100):
 
    if i ==0:
      hn.append(elist[0]*hn1 + hn2)
      kn.append(elist[0]*kn1 + kn2)
    elif i==1:
      hn.append(elist[1]*hn[0] + hn1)
      kn.append(elist[1]*kn[0] + kn1)
    else:
      hn.append(elist[i]*hn[i-1] + hn[i-2])
      kn.append(elist[i]*kn[i-1] + kn[i-2])
    #print i,")",hn[i],kn[i],float(hn[i])/kn[i]
print
print "The sum of the digits of the 100th continued fraction of e numerator is",sum(int(n) for  n in list(str(hn[99])))
print "Process time is ", time()-st

"""
print "!!", ee

print
print
print eval(estring),e
"""

