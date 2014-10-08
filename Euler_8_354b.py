#
#
#
#
#


from math import sqrt,sin,cos,pi
global f
f = 3**.5/2

'''
def d(p1,p2):

  f = 
'''
#[]

L=[0]*1001

for l in xrange(3,1000):

  N = int(l/f)+1
  #f = cos(pi/6)
  ctr = 0
  for x in xrange(-N,N+1):  #int(N/2**.5)):
    for y in xrange(-N,N+1):
      d = (x/2.)**2 + (y*f)**2
      #print x,y,d**.5

      #print x/2.,y
      if d==l:  #round(d**.5,6) == l:
        #print "!",x/2.,y
        L[l]+=1

print 
print L


