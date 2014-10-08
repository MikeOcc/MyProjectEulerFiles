#
#
#  Euler Problem 311
#
#
from math import sqrt

def IQ(ab,bc,cd,ad,bd,N):

  if ab**2 + bc**2 + cd**2 + ad**2 > N:return False
  if (2*ab**2 + 2*ad**2 - bd**2)<0:return False
  if (2*bc**2 + 2*cd**2 - bd**2)<0:return False
  m1 = ((2*ab**2 + 2*ad**2 - bd**2)/4)**.5

  m2 = ((2*bc**2 + 2*cd**2 - bd**2)/4)**.5
  #print m1, m2
  if m1 != int(m1): return False
  if m2 != int(m2): return False
  if m1 != m2:return False
  if m1 > bd/2: return False
  
  print "!",ab,bc,cd,ad,bd,":",m1,m2
  return True

##############

print IQ(19,29,37,43,48,10000)
ctr = 0
qset=[]
for a in xrange(1,51):

  for b in xrange(a+1,51):

    for c in xrange(b+1,51):

      for d in xrange(c+1,61):

        if a<b<c<d:
          for BD in xrange(a+d-1,d-a+2,-1):
               if BD%2>0:continue
            #for BD in xrange(b+c-1,c-b+2,-1):
               ctr += IQ(a,b,c,d,BD,10000)
               #qset.append(str(a)+str(",")+str(b)+str(",")+str(c)+str(",")+str(d))
               #if not (a,b,c,d) in qset:
               #  qset.append((a,b,c,d))
#qlist = list(set(qset))
print "set total is", len(qset)
print "total is", ctr