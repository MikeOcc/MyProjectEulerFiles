#
#
#  Euler Problem 283
#
#
from Functions3 import GCD,gcd
from math import sqrt
from Functions import divisors

def ta(a,b,c):
  A = (((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))**.5)/4
  return A

for m in xrange(1,10):
  f = 8*m**2
  fd = divisors(f)
  print m,f,fd
  ul = 2*m*2**.5
  for d1 in fd:
    if d1 <=ul:
      d2 = f/d1
      a = d1 + 4*m
      b = d2 +4 *m
      c = d1+d2+4*m
      A = ta(a,b,c)
      P = a+b+c
      print " :",d1, d2,":",a,b,c,":",A,P,A/float(P)



'''
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







