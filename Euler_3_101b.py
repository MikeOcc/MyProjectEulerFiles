#
#
#
#
#


def u(n):
  v=0
  for x in xrange(0,11):
    z = (-1)**x * n**x
    v += z
  return v
  
  
  
  
for i in xrange(1,11):
  print i, u(i)
  
  