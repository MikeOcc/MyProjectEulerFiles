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


f = cos(pi/6)

l=111**2 # L squared

print "Calculating honeycomb distances =",l**.5

N = 333

ctr = 0
for x in xrange(-N,N,3):
  for y in xrange(-N,N):
    d = (x/2.)**2 + (y*f)**2
    #print x,y,d**.5
    #if x==0 and y==2:print round(d,3)==3
    #print x,x/2.,y,d
    if round(d,6)**.5 == l**.5:
      print "!",x,y,":",x/2.,y*f, round(d,6)**.5
      ctr+=1

print 
print ctr




'''

N=111111111
N2 = N**2
for i in xrange(10**8,1,-1):
  b = i*f
  a = (N2 - (b)**2)**.5

  a1 = round(a,3)
  a2 = round(a*2,3)
  if a1 == int(a1) and round(a1**2 + b**2,3) == N2:
    print i, "a1", a1
  elif a2 == int(a2) and round((a2/2.)**2 + b**2,3) == N2:
    print i, "a2", a2
'''
