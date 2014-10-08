#
#
# Euler Problem 196
#
#
#

from Functions import IsPrime, RofPrimes
from time import time
from Euler import miller_rabin as p

def R(row):
  a = row * (row+1)/2

  b = a - row + 1

  return b,a

st = time()
#for i in xrange(1,12):
r = 7208785

s,e = R(r)  #5678027)  #  10000)
dp,dm = r,r-1

ro = (s%2 == 0 )

#5678027 7208785

print s, e, e-s

#exit()

'''
x = RofPrimes(s,e)

print x
print
print len(x)
'''
ctr=0
i = s + ro
tot = 0
while i<=e:
  if p(i):
    #print i, i+dp,i-dm+1
    n = 1
    
    if (i-dm)%2==0:
    
      if p(i-dm-1):
        n+=1
        #print "$",i,i-dm-1
        if p(i-dm-1-(dm-1)):
           n+=1 #;print "$--",i,i-dm-1-(dm-1)
        if p(i-2):n+=1 #;print "*--",i,i+2
    
      if p(i-dm+1):
        #print "$$",i,i-dm+1
        n+=1
        if p(i-dm+1-(dm-1)):
           n+=1 #;print "$$-+",i,i-dm+1-(dm-1)
        if p(i+2):n+=1 #;print "*-+",i,i+2
    
      if p(i+dp):
        #print "$$$",i,i+dp
        n+=1
        if p(i+dp*2-0):n+=1 #;print "$$$-",i,i+dp*2-0
        if p(i+dp*2+2):n+=1 #;print "$$$+",i,i+dp*2+2
    
    else:
      
      if p(i-dm):
        #print "#",i
        n+=1
        if p(i-dm-(dm-1)-1):
          n+=1
          #print "#!@1",i
        if p(i-dm-(dm-1)+1):
          n+=1
          #print "#!@2",i

      if p(i+dp-1):
        n+=1
        #print "#",i
        if p(i+dp*2):
          n+=1
          #print "#!@",i
        if p(i-2):
          n+=1

      if p(i+dp+1):
        #print "#",i
        n+=1
        if p(i+dp*2+2):
          n+=1
          #print "#+#",i
        if p(i+2):
          n+=1

    if n> 2:
      tot += i;ctr+=1
      #print "!",ctr,i,n

  i += 2

print
print tot
print "process time -",time() - st



