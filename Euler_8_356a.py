from math import cos, acos,pi
n=2 

#p = -b**2 => -(-2**n)**2/(3)
#q = (2*b**3 +27*d)/27
#  = (2*(-2**n)**3 + 27*n)/27

b = -2**n
d = n

p = -b*b
q = (2*b*b*b + 27 * d)/27.

print p, q
#print q*q/4. + p*p*p/27.
'''
u1 = -q/2. + (q*q/4. + p*p*p/27.)**.5
v1 = -q/2. - (q*q/4. + p*p*p/27.)**.5

if u1 < 0:
  u = -abs(u1)**(1/3.)
else:
  u = u1**(1/3.)

if v1 < 0:
  v = -abs(v1)**(1/3.)
else:
  v = v1**(1/3.)

t1 = u + v
'''

theta = acos((3*q)/(2*p)*(-3/p)**.5)
k=2
t1 = 2*((-p/3.)**.5)*cos(theta/3.-k*2*pi/3.)
x = t1 - b/3.
print ########
print n, b, d
print p,q
print t1
print "!",t1*t1*t1 + p*t1 + q
print x