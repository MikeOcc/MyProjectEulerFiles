#
#
# Euler Problem 295
#
#


def ip(r):

  retval = 0
  for x in xrange(0,int(r)+1):
    y = round((r**2 - x**2)**.5,5)
    if int(y)==y:
      retval +=1
      print x, int(y)

  return retval

for j in xrange(1,10**8+1):
   z = ip(j**.5)
   if z> 0:
     print j,")"
     print






