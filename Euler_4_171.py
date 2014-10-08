#/python/Euler_4_171.py
#  Euler Problem 171
#

def f(n):

  nl = list(str(n))
  return sum([int(i)**2 for i in nl ])
  

lst = []

LIM = 10**20      #0

#for i in xrange(LIM,LIM-100,-1):
i=0
while i< 10000000:
  j = LIM - i
  x = f(j)
  if  int(x**.5)**2 ==x:
    #print j,x
    setj = set(str(j))
    print j,x,setj
  i+=1
