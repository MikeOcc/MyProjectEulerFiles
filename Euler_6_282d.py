#
#
#  Euler Problem 282
#  Ackermann's Function
#
#
from time import time

#
#  Split Ackermann's function by variable m and simplify to avoid recursion issues.
#
def A(m,n):

  if m==0: 
     return n+1

  if m==1:
     return (n+2)
	 
  if m==2:
     return (2*n + 3)

  if m==3:
     return (2**(n+3)-3)  

  if m==4:
     return towerMod(n) - 3

  if m==6:
     if n>8:n=8
     return A(5,n+1)
	 
	 
  if m>0 and n==0:
     return A(m-1,1)
  
  else:

     return A(m-1,A(m,n-1))

def modpow(base, exponent, modulus):
#
#  Function to determine the modulus of a power function
#
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result


def towerMod(n):
#
#  Expoentiation va Euler's Method
#  Phi(14**8)->Phi(7**8) = 7**8*6/7 = 4941258
#

  # if n>7 treat as n==7 due to convergence
  if n>7:n=7
  
  # Count down the power level till n1 == 1.  
  n1=n+2
  
  x=2
 
  while n1 >0:

    if n1==1:
      x=pow(2,x,14**8)	
    else:
      x=modpow(2,x,4941258)	
	
    n1-=1
  
  return (x)
  

# Calculate start time of procedure
st = time()

# Initialize sum
summ = 0
modval = 0

for n in xrange(7):
  modval = A(n,n)
  # print value for each n and note convergence for n>4
  print "n:",n,modval
  summ += modval
  

#print 6,A(5,5)
#summ += A(5,5)
# Take modulus of summation
summ %= 14**8

print "The result of the sum of A(n,n) for n=0 to 6 mod 14**8 is", summ
print "Time elapsed in seconds is ", time() - st


