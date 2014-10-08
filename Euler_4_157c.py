
#
#  Problem 157
#
from time import time

def diophantine(a,b,P,n):

  #10**n*b = a * (b*P - 10**n)
  # a = 10**n*b/(b*P - 10**n)
  return 10**n*( b + a)==a*b*P

#for i in xrange(1,10):

st = time()
n= 1
a,b =0,0
N = 4

ctr = 0
for n in xrange(1,N+1):
  tenN = 10**n
  for P in xrange(1,2*10**n+1):
    #bmax = int(tenN*1./P)
    #print "bmax",bmax
	# print "P:",P
    # print
    for b in xrange(1,4000+1):
        if (b*P - tenN <= 0):continue
      #for a in xrange(1,b+1):
        a = tenN*b/(b*P - tenN)
        if a>b:continue
        if diophantine(a,b,P,n):
          ctr+=1
          print ctr,P,tenN,")",b,a
          #break


print "Total for n<=",N,"is", ctr
print "Process time is", time() - st
