#x^2 - 61b^2 = 1
#
#start with b=1
#find next square
#8^2 - 61 = 3   triplet (8,1,3) X (m,1,m^2-61) = (8m+61,8+m,3*(m^2-61))

from math import sqrt

def FNHSQ(n):
  z = n
  
  while True:
    y = int(z**.5) + 1
    #print int(z**.5),y,z
    return y*y

def FindM(aa,bb,kk,D):
   dmin = 10**8;bestm=1

   for t in range(-100,100):
     m = -kk*t + 1
     if (aa*m+ D*bb)/kk == int((aa*m+D*bb)/kk):
        dmin1 = abs( m*m -D )
        if dmin1 < dmin:
          dmin = dmin1;bestm=m
     print "!",t,m  

   print "Mfound", bestm
   return bestm
  

 

###################

def GetX(D):
  #D=61
  k = 1
  a = 1
  b = 0
  a1 = 1
  #a = int(sqrt(FNHSQ(D)))
  sqrtd = sqrt(D)
  m=1

  while k!=1 or b==0:

    #find next highest square
 
    #k= a*a - k*b*b
    print "#####################"
#    m = FindM(a,b,k,D)
    print "!",k,sqrtd,m
    m = k * (m/k+1) - m  #  -m/(k+1)   #
    m = m - int((m - sqrtd)/k) * k
    print "!!",m
    a = (m*a1 + D*b)/abs(k)
    b = (m*b + a1)/abs(k)
    k = (m*m-D)/k

    a1 = a  

    #print a1/3.,b1/3.,k1/3.
    #a,b,k0= a1/3./4.,b1/3./4.,k1/3./4.

  return a

if __name__=='__main__':

  maxx = 0,Dfound =0
  for D in xrange(1,1001):
    x = GetX(D)
    if x> maxx:
      maxx=x,Dfound = D
  
  print "D for largest X =",maxx,"is", Dfound
