#
#


from Functions import RofPrimes

def notcoprime(cp,Y):
  for yy in Y:
    if gcd(yy,cp)!=1:
      return yy
  return -1

MX=30  #200000
x = RofPrimes(2,MX)
#x.append(1)

def fn(T,Sum,mn):
   NewSum=[]
   NewFactor=[]
   S=list(T)
   S.remove(1)
   S1=list(S)
   for i in S:
     p=0
          

T=[1,2,3]
Sum=6

p=2







