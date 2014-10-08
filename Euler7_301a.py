#
#
#  Euler 301
#


def X(a,b,c):

  return a^b^c


def fibo(n):
  #if n ==0:return 0
  if n ==1:return 2
  if n ==2:return 3
  return fibo(n-2) + fibo(n-1)



#############

nmax=30

for j in xrange(1,nmax+1):
  cnt = 0
  for i in xrange(1,2**j+1):
     r=(X(i,i*2,i*3)==0)
     cnt+=r
     #print i,r
 
  print "answer for n =",(j,2**j)," is", cnt

print "Fibo(j) is",fibo(30)