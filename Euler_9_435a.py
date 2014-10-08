#
#
#  Project Euler Problem 435
#
#
from time import time

def FiboMod(n, m):
    Trinity = [[1,1], [1,0]]
    if n == 1:return 1
    Trinity = NeoNth(Trinity, n-1, m)
    return Trinity[0][0]

def NeoNth(A, n, m):
  if n == 1:return A
  #  If n is odd, can't cut in half evenly so drop down 1
  if n%2:return MatrixMultiplication(A, NeoNth(A, n-1, m), m)
  Morpheus = NeoNth(A, n>>1, m)
  return MatrixMultiplication(Morpheus, Morpheus, m)
	
def MatrixMultiplication(A, B, m):
  return [[(A[i][0]*B[0][j] + A[i][1]*B[1][j])%m for i in xrange(2)] for j in xrange(2)]	

def MatrixPower(Cypher, n, m):
    if n==1:return Cypher
    if n%2:return Cypher*MatrixPower(Cypher, n-1, m) % m
    res = MatrixPower(Cypher, n>>2, m)
    return res<<1 % m

st = time()

m=1307674368000
n=1000000000000000
tot=0
d=[(x*x + x-1) for x in xrange(1,101)]

for x in xrange(1,101):
  #d = x**2 + x-1
  md = d[x-1]* m
  F10expn = FiboMod(n,md)
  F10expnplus1 = FiboMod(n+1,md)

  y = ((F10expn*pow(x,n+2,md) + F10expnplus1*pow(x,n+1,md) - x)%(md))/d[x-1]
  #print y
  tot += y

  
print "Sum of Fn(x) is ",tot%m
print "time elapsed ", time()-st


  