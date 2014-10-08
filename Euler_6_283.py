#
#
#  Euler Problem 283
#
#
from Functions3 import GCD,gcd
summ = 0
ctr,ctr1 = 0,0
for m in xrange(2, 4000):
  for n in xrange(1, m):
    if gcd(m,n)!=1 or (m-n)%2==0: continue
    a = (m*m - n*n)
    b = 2*m*n
    c = (m*m + n*n)
    #if GCD((a,b,c))>1:continue
    #print m,n,":",a,b,c 
    
    #if a**2 +b**2 == c**2:
    A0=a*b/2;P0=a+b+c;R=float(A0)/P0
    ctr+=1
    #print m,n,":",a,b,c,":",A0,P0,R
    if R < 1001: 
      #print a,b,c,":",A0,P0,R
      #summ += P0

      i=1

      while 1:
        A = A0*i**2
        P = P0*i
        R = float(A)/P
        if R==int(R) and R<1001:
          print m,n,i,":",a*i,b*i,c*i,":",A,P,R
          summ += P
          ctr1+=1
        if R>1000:
          break
        i+=1

print "answer is",summ
print "total # triangles",ctr
print "total # Ts with int R", ctr1
exit()
'''

A0 = 24
P0 = 24
R=1
i=2
Psum = 0
print 1,A0,P0
while 1:
  A = A0*i**2
  P = P0*i
  R = int(float(A)/P)
  if R <1000:
    print i,A,P, R
    Psum += P
  else:
    break
  i+=1

print
print "Sum of perimeters is", Psum
'''









