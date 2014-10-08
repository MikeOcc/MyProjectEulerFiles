#
#  Euler Problem 311
#
#
#from math import sqrt

def IQ(ab,bc,cd,ad,D,N):

  if ab**2 + ad**2 != bc**2 + cd**2:return False

  if ab**2 + ad**2 > N/2:return False

  bd=D/2.

  if ((ab**2 + ad**2)/2 - bd**2)<0:return False
  if ((bc**2 + cd**2)/2 - bd**2)<0:return False

  #m1 = ((2*ab**2 + 2*ad**2 - bd**2)/4)**.5
  #m2 = ((2*bc**2 + 2*cd**2 - bd**2)/4)**.5

  m1 = ((ab**2 + ad**2)/2. - bd**2)**.5
  m2 = ((bc**2 + cd**2)/2. - bd**2)**.5

  #print m1, m2

  if (m1 != int(m1)) or (m2 != int(m2)): return False

  if m1 != m2:return False

  if m1 > bd: return False
  
  print "@",ab,bc,cd,ad,bd*2,":",m1,m2,ab**2 + bc**2 + bc**2 + cd**2,ab+ad-bd*2
  return True

##############
N=1000000
#print IQ(19,29,37,43,48,10000)
#print IQ(26, 31, 46, 49, 74,10000)
ctr = 0
qset=[]
ctr2=0
for a in xrange(11,46):

  for b in xrange(a+1,58):

    for c in xrange(b+1,74):

      for d in xrange(c+1,100):
        
        if a<b<c<d:
          for BD in xrange(a+d-1,d-a+2,-1):
               ctr2+=1       
               if BD%2>0:continue
               ctr += IQ(a,b,c,d,BD,N)
               #qset.append(str(a)+str(",")+str(b)+str(",")+str(c)+str(",")+str(d))
               #if not (a,b,c,d) in qset:
               qset.append(BD)
qlist = list(set(qset))
print "set total is", len(qlist)
print "total is", ctr
print "total checks is",ctr2