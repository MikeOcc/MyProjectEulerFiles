#
#
#  Euler 355
#
#
from Functions3 import gcd,GCD
from itertools import combinations
from Functions import RofPrimes,RetFact,IsPrime
from math import log
from time import time


def Sum(L):
  return sum(L)

def notcoprime(cp,Y):
  for yy in Y:
    if gcd(yy,cp)!=1:
      return yy
  return -1


#################
st=time()

#for MX in range(200000, 200001):

for MX in range(30, 31):

  x= RofPrimes(2,MX)
  y=list(x)
  tmp=[]
  tmpr=[]
  for y1 in x:
    z = log(MX)/log(y1)
    z1 = y1**int(z)
    #print y1, z1
    tmp.append(z1)
    tmpr.append(y1)

  #exit()
  
  for z in tmp:
    x.append(z)
  for z in tmpr:
    x.remove(z)

  x = sorted(x)
  x.append(1)

  y = sorted(y,reverse=False)

  for z in y:

    p = 0
    nprev,zprev,Oprev=0,0,0
    makechange = False
    vlog = log(MX)/log(z)
    vmax = z**int(vlog)
    #print "#$",z,vmax
    while 1:
      p+=1
      v = z**p
      vsing = z**int(log(MX)/log(z))
      #print "v1",z,v,p
      if v> MX:
          #print "v",z,p,v
          break
      #if z==3 and p==4: print "YEAH"
      '''
      if v>MX*.8:
        #print "v!!!!",z,p,v,x
        if v in x:
          makechange = False
          break
        else:
          hunt= notcoprime(z,x)
          print "hunt",z, x, hunt
          if hunt>0 and hunt!=v:
            facts=RetFact(hunt)
            x.remove(hunt)
            for fs in facts:
              if fs!=z:
                x.remove(fs)
            x.append(v)
          
          else:
            #x.remove(z)
            #x.append(v)
            break         
      '''
      for zz in x:
        New = v * zz
        if New >= MX:break
        Old1 = notcoprime(v,x)
        #if z == 2:
          #print v,zz,New, Old1,":",v*zz,Old1+zz
        Prev = Old1 + zz
        
        #print New>Prev
        if New > Prev:
          makechange = True
          if zprev + New > nprev + zz:
           nprev=New
           zprev=zz
           Oprev=Old1
    print vsing,zz,nprev
    if vsing>=int(MX*.9):
       print "grrr"
       if vsing not in x:print "GRRRRRRR"
       makechange = False
    if makechange == True:
      print z,Oprev
      x.remove(Oprev)
      x.remove(zprev)
      x.append(nprev)

  #x.append(1)
  #print sorted(x)
  #print MX,":",sorted(x),":",Sum(x)
  print MX,":",x,":",Sum(x)

print "Process time is", time()-st

for i in x:
  if not IsPrime(i):   #print i  # i%2==0:
    print i,RetFact(i)
