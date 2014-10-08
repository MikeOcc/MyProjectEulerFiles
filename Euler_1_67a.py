#
#  find maximal sum in triangle.txt
#

from time import time
from string import whitespace,strip,replace

st = time()
f = open('triangle.txt','r') # Number pasted to file.

i = 1
ctr=0

y = [ [0 for col in range(100) ] for row in range(100)]

for i in range(0,100):
  
  x= replace(strip(f.readline())," ",",")
  z = x.split(",")
  lz = len(z)
  for j in xrange(lz):
    y[i][j] =  int(z[j])

for i in xrange(98,0,-1):
  max1, maxr = 0,0
  for j in xrange(0,i):
    b = y[i+1][j] ; c = y[i+1][j+1]
   
    if b > c:
      y[i][j] += b
    else:
      y[i][j] += c

f.close()

print
print "The answer for the maximal path of the triangle is", y[0][0] + max(y[1][0],y[1][1])
print "Process time is", time()-st

print y[1][0],y[1][1]
print
for i in xrange(100):
  for j in xrange(i+1):
    print y[i][j],
  print 

