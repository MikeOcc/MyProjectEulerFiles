
#
#  Problem 157
#
from time import time

def diophantine(a,b,P,n):

 return 10**n*( b + a)==a*b*P

#for i in xrange(1,10):

st = time()
n= 1
a,b =0,0
N = 9

ctr = 0
for n in xrange(9,N+1):
  print "N:",n
  Npow = 10**n
  for p in xrange(1,2* Npow +1):
    a1 = float(Npow)/float(p); astart = int(a1); aend = (2*astart)
    print "ASTART:",astart,Npow,p
    if astart < 1:astart=1
    aend = astart * 2
    for a in xrange(astart,aend +2):
      if (a*p-Npow)> 0:
        b= (a* Npow) /(a*p -Npow)     # 
      if a<=b and diophantine(a,b,p,n)==True:
        ctr+=1
        print ctr,") P,a,b:",p,a,b,"a1:",a1   # ,10**n
      #elif p in (8000,10023,10060):
      #  print "!!!", p, a1, p/a1
      if a1<1:break

print "Total for n<=",N,"is", ctr
print "Process time is", time() - st
