#
#
#  Euler Problem 309
#
#

#
#  h = intersection height
#  l = long ladder
#  s = short ladder
#  
#  f(x) = x^4 + bx^3 + cx^2 -dx - e
#  f(x) = x**4 + 2*h*x**3 + (l**2 - s**2)*x**2 - 2 * h**3*x - h**4 == 0
#  c = l**2 - s**2 
#  d = 2 * h**3
#  calc  h + x
#  w = sqrt(s**2 - (h+x)**2) => (h+x) = sqrt(s**2 - w**2)

from math import sqrt
from time import time

st = time()
def solvq(l,s,h):
  h1 = h
  b,c,d,e=2*h,(l**2 - s**2),2 * h**3,h**4
  for x in xrange(s/2,1,-1):
    #x = float(x0)
    #h = float(h)
    #l = float(l)
    #s = float(s)
    #y = x**4 + 2*h*x**3 + (l**2 - s**2)*x**2 - 2 * h**3*x - h**4
    y = x**4 + b*x**3 + c*x**2 - d*x - e
    #print "!",y
    if y ==0:
      h1 += x
      if h1 < s:
        return int(h1)
      else: 
        return 0
  return 0

#####################
tot = 0
lim = 500
cl=[0]*(lim+1)
cl1=[(0,0,0,0)]*(lim+1)
for x in xrange(104,lim):
  if cl[x]==1:
    print cl1[x]
    continue
  elif cl[x]==-1:
    continue 
  isfound = False
  for y in xrange(69,x):
    for H in xrange(21,y/2+1):
      de = solvq(x,y,H)
      if de > 0:
        w = sqrt(y**2 - de**2)
        if w == int(w):
          print x,y,H,":",de,":",w
          n = lim/x
          ctr=1
          while ctr<=n:
            cl[x*ctr]=1
            cl1[x*ctr]=(ctr*x,ctr*y,ctr*H,ctr*w)
            tot +=1
            ctr +=1
          isfound = True
        #else: print "false find",x,y,H,de
        #if isfound == False:
        #  n = lim/x
        #  ctr=1
        #  while ctr<=n:
        #    cl[x*ctr]=-1 
        break
    if isfound:
      break
  #if isfound == False: 
  #   #print "!!",x,y,H   
  #   n = lim/x
  #   ctr=1
  #   while ctr<=n:
  #     cl[x*ctr]=-1 
  #     ctr+=1
print "Total # of solns is", tot
print "Process time is", time()-st