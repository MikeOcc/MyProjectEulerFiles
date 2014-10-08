


def Fib(n,m):

  F = [ [ 1 for i in range(2) ] for j in range(2) ]
  F[1][1] = 0
  if (n == 0):
    return 0
  power(F, n-1,m)
 
  return F[0][0];

 
def multiply(F, M,m):

  x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]
  y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]
  z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]
  w =  F[1][0]*M[0][1] + F[1][1]*M[1][1]
 
  F[0][0] = x %m
  F[0][1] = y %m
  F[1][0] = z %m
  F[1][1] = w %m

 
def power(F, n,m):

  M = [ [ 1 for i in range(2) ] for j in range(2) ]
  M[1][1] = 0
 
  # n - 1 times multiply the matrix to {{1,0},{0,1}}
  for i in xrange( 2, n+1):
    multiply(F, M,m)

def mat_mult(A, B, m):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= m
    return C
 
def mat_pow(A, p, m):
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p-1, m), m)
    X = mat_pow(A, p//2, m)
    return mat_mult(X, X, m)
 
def fib2(n, m):
    T = [[1,1], [1,0]]
    if n == 1:
        return 1
    T = mat_pow(T, n-1, m)
    return T[0][0]
 
def mpow(x, p, m):
    if p == 1:
        return x
    if p % 2:
        return x*mpow(x, p-1, m) % m
    r = mpow(x, p//2, m)
    return r*r % m
 
#def F(n, x, m):    

#for i in xrange(10**15-10,10**15+1):
m=1307674368000
n=10**15
F10expn = fib2(n,m)
F10expnplus1 = fib2(n+1,m)
tot=0
# x=11
# tot = ((F10expn*pow(x,n+2,m) + F10expnplus1*pow(x,n+1,m) - x)%(m*(x**2 + x -1)))/(x**2 + x -1)

# print tot%1307674368000
# exit()
for x in xrange(1,101):

  F10expn = fib2(n,m*(x**2 + x -1))
  F10expnplus1 = fib2(n+1,m*(x**2 + x -1))

  y = ((F10expn*pow(x,n+2,m*(x**2 + x -1)) + F10expnplus1*pow(x,n+1,m*(x**2 + x -1)) - x)%(m*(x**2 + x -1)))/(x**2 + x -1)
  #y = ((F10expn*pow(x,n+2,m) + F10expnplus1*pow(x,n+1,m) - x))/(x**2 + x -1)
  print y
  tot += y
  #tot %= m
  
print "Result ",tot%1307674368000


  