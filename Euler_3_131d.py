#
#  Euler problem 131
#
#  []


from Functions import IsPrime
from time import time

st = time()
cubes = [i**3 for i in xrange(1,10**6)]

N=10**10

ctr=0
ctr1 = 0
for j in xrange(0, len(cubes)):
  ctr1+=1
  cub1,cub2 = cubes[j],cubes[j+1]
  pposs = cub2 - cub1

  if IsPrime(pposs) and pposs<N:
    cub3 = int(round((cubes[j]**3 + cubes[j]**2*pposs)**(1/3.),4))
    #print ctr+1,") ",cubes[j],cub3,":", pposs
    ctr+=1
  if pposs>N:break

print "total is", ctr 
print "process time is" , time()-st
print "number of loops", ctr1



