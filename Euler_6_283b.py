#
#
#  Euler Problem 283
#
#
from Functions3 import gcd
from math import sqrt
from Functions import divisors

def ta(a,b,c):
  A = (((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))**.5)/4
  return A
summ = 0

#
#  Using Heron's formula from Lubomir Markov's extension of Goehl's Method
#
M=[]
for m in xrange(1,1001):
  print "m:",m,
  psum = 0
  #u = 2*m
  fd0 = divisors(2*m)   # Factoring u = 2m
  for u in fd0:
    ul = u*3**.5         # choosing factors up to u*sqrt(3)
    mxul = int(ul)+1
    for v in xrange(1,mxul):
      if gcd(u,v)!=1:continue     # choosing v coprime to u
      f = 4*m*m*(u*u +v*v)        # = delta1 * delta2
      fd = divisors(f)            # obtaining factors for d1,d2
      ul2 = 2*m*((u*u+v*v)**.5)   # obtaining sqrt to avoid repetitions
      #print "!",m,u,v             # showing m,u,v for curiosity's sake
      for d1 in fd:
        if ((2*m)*(v**2-u**2)/u)<= d1 <=ul2:  #choosing range of delta1 to ensure A=mP
          d2 = f/d1
          a = (d1+2*m*u)/v + (2*m*v)/u
          b = (d2+2*m*u)/v + (2*m*v)/u
          c = (d1+d2+4*m*u)/v
          A = ta(a,b,c)
          P = a+b+c
          R = A/float(P)    # paranoid check to ensure ratios match
          if R==int(R):     # Making sure Ratio is integer,probably not necessary
            summ +=P
            psum +=P
            #print "m:",m,d1, d2,":",a,b,c,":",A,P,R  
            # I like looking at the numbers to see if there are any obvious patterns
            #print P,
            #print
  print psum,
  print  
  M.append(psum)
print
print
print "Sum of Perimeters of Heron Triangles ->m=1000 is",summ
print
print
print M








