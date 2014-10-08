#
#
#  Euler Problem 239
#
#

from math import factorial

def prob(n) :


  f = [factorial(i) for i in xrange(101)]

  p=[0]*101
  p[0]=1
  for i in xrange(1,n+1):  
     p0 = 1.0

     for k in xrange(1,i+1): 

       p0 -= p[i-k]/f[k]
                    
     p[i]=p0
  
  return p

l = prob(100)

#print l

for i in xrange(20):
  print i,l[i]
print

summ = 0
n = 1.0 / (98 * 9900)

for k in xrange(76):
  if k >0:n*= (1.0 /(97-k+1))*(75-k+1)/k
  summ += l[97-k] * n

print "The probability is ", (25.*24*23/3/2/1)*summ
	
  