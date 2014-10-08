#
#
#  Euler Problem 64
#
from math import *

def GetCFList(n):   #  get continued fractions list
  nn=n
  a = []
  fln = int(sqrt(n))
  d = [1]
  m = [0]
  a.append(fln)
  #print "mm,dd,a",m,d,a

  for i in range(1,300): 
    mm=d[i-1]*a[i-1]-m[i-1]
    dd=(nn-mm*mm)/d[i-1]
    m.append(mm)
    d.append(dd)
    aa=int((a[0]+m[i])/d[i])
    #print "mm,dd",mm,dd,aa

    a.append(aa)
    
  return a




if __name__=='__main__':
  summ=0
  maxlen=0
  for N in xrange(2,10001):
  
    z = int(sqrt(N))
    if z== sqrt(N):continue
    x = GetCFList(N)
    print N,x
    
    xx = set(x[1:])
    xlen=len(xx)
    mtch=[]
    
    for j in range(1,300):
      if x[j] in xx:
        mtch.append(x[j])
        xxx=set(mtch)
        #print xx,xxx
        if xxx == xx:
          #print mtch
          a=len(mtch)
          b=len(mtch)
          if a>maxlen:maxlen=a
          print a,b
          if (not (a/2. == int(a/2))) or a==1:
            summ+=1
          print mtch
          break
  print "Number of Odd periods is",summ,maxlen
   
       