
def d(n):
  from math import floor,sqrt

  #print n,

  if n==1: return 0 
  else:    r=floor(sqrt( n) )   # first take into account the case that n is a perfect square.  if r*r==n:
     sum1=1+r 
     r=r-1 
  else:
     sum1=1

  if float(n)/2. != n/2 :
     f=3; step=2
  else:
     f=2; step=1

  while f<=r:     if n%f==0:
       sum1+= f+ (n/f)     f+= step

  #print sum1  return sum1


def abundantsum(i): 
  return any(i-a in abundants for a in abundants) 


if __name__ == "__main__":

  abundants = set(i for i in range(1,28124) if d(i) > i) 

  print sum(i for i in range(1,28124) if not abundantsum(i))




