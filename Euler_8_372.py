#
#
#  Euler Problem 372
#
#



def R(M,N):
  ctr = 0
  for x in xrange(M+1,N+1):
    for y in xrange(M+1,N+1):
      f = x**2/y**2
      if f%2==1:
        print x,y,f
        ctr+=1

  return ctr


#print R(0,100)
print R(100,10000)

