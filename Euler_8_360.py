#
#
#  Euler Problem 360
#
#

def d(x,y,z):

  return (x**2)**.5 + (y**2)**.5 + (z**2)**.5  

ctr = 0
summ = 0

R=45  #10**4

for r in xrange(R,R+1):
  ctr = 0
  summ = 0
  for x in xrange(-r,r+1):
    for y in xrange(-r,r+1):
      v = r**2 - x**2 - y**2
      if v<0 or v**.5!=int(v**.5):continue
      z = (v)**.5
      if z==int(z):
      #if x**2 + y**2 + z**2 == 45**2:
        #print x,y,z
        if z==0:
           ctr+=1
           summ += d(x,y,z)
        else:
           ctr+=2
           summ += 2*d(x,y,z)
  print 
  print r,ctr,summ
  #print summ








