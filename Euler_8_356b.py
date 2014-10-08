from math import cos
from decimal import Decimal


def newt(n):

   roots = []
   b = float(2**n)
   bp = 2*b
   d = float(n)
   A0=-1
   A=A0
   while 1:
     #print A
     #if A==0:A=1
     for x in xrange(1000):
       A -= (A**3 -b*A**2 + d)/(3.*A**2 -bp*A )
       #A -= (A*A)*(A**3 -b*A**2 + d)/(3.*A**2 -bp*A ) 
       #print A0,x, A
       #if A**3 -b*A**2 + d==0:break
     #print
     if 1: # (A**3 -b*A**2 + d==0):
       if A not in roots:
         match=False
         for r in roots:
           if round(r,9)==round(A,9):
             match = True
         if match == False:
           roots.append(A)
           print "!!!",A, roots
           print
     if A0==-1:A0=1
     else: A0+=1
     A = A0
     if len(roots)==2:
       #print "time to break"
       break
   print "Roots:",roots
   print "A0",A0
   return max(roots)
    
def cubic(a, b, c, d=None):

  if d:	 # (ax^3 + bx^2 + cx + d = 0)
    a, b, c = b / float(a), c / float(a), d / float(a)
    t = a / 3.0
    p, q = b - 3 * t**2, c - b * t + 2 * t**3
    u, v = quadratic(q, -(p/3.0)**3)
    if type(u) == type(0j):	# complex cubic root
      r, w = polar(u.real, u.imag)
      y1 = 2 * cbrt(r) * cos(w / 3.0)
    else:  # real root
      y1 = cbrt(u) + cbrt(v)
    y2, y3 = quadratic(y1, p + y1**2)

  return y1 - t, y2 - t, y3 - t

def delta(a,b,d):

  return -4*b**3*d - 27*a**2*d**2

def g(n):
  pass
#   x**3 - 8x**2 + 2 = 0
#   x2*(x-8)+2= 0
#   a = 1,b=8,c=0,d=2  
#   while 1:
     
'''
for n in  xrange(1,31):
   b = -2**n
   d = n
   a = 1
   #print n, delta(1,-2**n,n)
   f1= ((2*b**3 +27*d)**2-4*b**2)**.5
   p = -b/3.
   q = p**3 -d/2
   r = 0
   #x = (q + (q**2 +(-p**2)**3)**.5)**(1/3.) + (q - (q**2 +(-p**2)**3)**.5)**(1/3.) + p


   print n, f1
'''
'''
a = 3.86619826
b = a
for i in xrange(1000):
  b*=a
  #b=b%10*16
  print i, int(b)%10**8
'''
#print cubic(1,-8,0,2)

for v in xrange(19,30):
  print v,Decimal(newt(v))
  print

