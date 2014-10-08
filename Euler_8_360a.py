#
#
#  Euler Problem 360
#
#

def d(x,y,z):

  return (x**2)**.5 + (y**2)**.5 + (z**2)**.5  

ctr = 0
summ = 0

R=45 #10**4

for x in xrange(-0,R+1):
  for y in xrange(-0,R+1):
      v = R**2 - x**2 - y**2
      if v<0 or v**.5!=int(v**.5):continue
      z = (v)**.5
      if z==int(z):
      #if x**2 + y**2 + z**2 == 45**2:
        print x,y,z
        if z==0:
           ctr+=1
           summ += d(x,y,z)
        else:
           ctr+=2
           summ += 2*d(x,y,z)
print 
print ctr
print summ








