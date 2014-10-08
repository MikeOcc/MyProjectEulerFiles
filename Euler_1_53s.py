#Dim a, b(100, 100), c, x, y As Integer
#For a = 0 To 100
#  b(a, 0) = 1
#  b(a, a) = 1
#Next a
#c = 0
#For x = 1 To 100
#  For y = 1 To x - 1
#    b(x, y) = b(x - 1, y) + b(x - 1, y - 1)
#    If b(x, y) > 1000000 Then
#      b(x, y) = 1000000
#      c += 1
#    End If
#  Next y
#Next x

from math import factorial
from time import time
st = time()

a = 0
ctr = 0
#x = 0
#y = 0

b = [ [0 for col in range(101) ] for row in range(101)]

for a in range( 0 , 100):
  b[a][ 0] = 1
  b[a][ a] = 1


for x in range( 1, 101):
  for y in range(1,x):

    d = b[x - 1][y] 
    e = b[x - 1][y - 1]
    #print "d,e:", x,y,d,e
    b[x][y] = d + e
    #print "bxy:",b[x][y]
    if b[x][y] > 1000000:
      b[x][y] = 1000000

      ctr += 1

#print b

print "Number of values of nCr > 10**6 is", ctr
print "Process times is ", time() - st
