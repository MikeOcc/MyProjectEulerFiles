

'''
# calculate fib
def mul(A, B):
    def f(i, k):
        return sum(A[i][j] * B[j][k] for j in xrange(nb)) % D
 
    na = len(A)
    nb = len(B)
    mb = len(B[1])
    return [ [ f(i, k) for k in xrange(mb) ] for i in xrange(na) ]
 



print mul(0,1)
'''


fn=0
fn1 = 1
from mpmath import sqrt,power,mp,mpf
for i in range(0,1000):
  mp.dps = 10000
  one = mpf(1)
  two = mpf(2)
  five = mpf(5)
  if i == 0: y=0
  elif i==1: y=1
  else:  
    y=(fn1 + fn)
    fn=fn1
    fn1=y 
  x = round((one/sqrt(five))*(power((one+sqrt(five))/two,i)-power((one-sqrt(five))/two,i)),3)
  temp = x
  print i, int(x) 
  print "  ",y       #":", (x)-y
  print
#% 1234567891011

