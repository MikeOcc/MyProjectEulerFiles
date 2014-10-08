
#
#  Problem 157
#
from time import time
from math import floor
from math import ceil
from Functions import RetFact

def diophantine(a,b,P,n):

  #10**n*b = a * (b*P - 10**n)
  # a = 10**n*b/(b*P - 10**n)
  return 10**n*( b + a)==a*b*P

#for i in xrange(1,10):

st = time()
n= 1
a,b =0,0
N = 9

ctr = 0
for n in xrange(9,N+1):
  tenN = 10**n
  for P in xrange(1,2): #2*10**n+1):
    bmin = int((tenN*1./P)+1)
    if bmin==0:bmin=1
    #print "bmax",bmax
    #print "P:",P,bmin
    # print
    for b in xrange(bmin,2*tenN+1):
        # if (b*P - tenN <= 0):
          # print "neg",b,P,tenN
          # continue
      #for a in xrange(1,b+1):
        a = tenN*b/(b*P - tenN)
        if a<b:continue
        if diophantine(a,b,P,n):
          ctr+=1
          print ctr,P,tenN,")",b,a,":",RetFact(b),RetFact(a)
          #break
  print n,ctr

print "Total for n<=",N,"is", ctr
print "Process time is", time() - st
