#
#
#  Euler 401
#
#
from time import time

def sumSquares(x):
  return (2*pow(x,3)+3*pow(x,2) + x)/6
  #return (2*x**3+3*x**2 + x)/6
  #return (x*(2*x+1)*(x+1))/6

  
st = time()

summ = 0
lim = 10**15
i = 1
pv=-1
while i <= lim:
  mult = lim/i
  next = lim/mult+1
  summ += mult * (sumSquares(next-1) - sumSquares(i-1))
  i = next
  summ %= 10**9
  # if summ>10000 and pv==summ:
    # print i,summ
  # else:
    # pv=summ

print "answer is ", summ%10**9
print "time elapsed", time()-st