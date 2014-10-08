#Problem 304
#03 October 2010
#
#For any positive integer n the function next_prime(n) returns
# the smallest prime p such that p>n.
#
#The sequence a(n) is defined by:
#   a(1)=next_prime(1014) and a(n)=next_prime(a(n-1)) for n>1.
#
#The fibonacci sequence f(n) is defined by: 
#  f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.
#
#The sequence b(n) is defined as f(a(n)).
#
#Find sum(b(n)) for 1 <=n <= 100000. Give your answer mod 1234567891011.
#


def next_prime(n):

  from Functions import IsPrime

  if n==1:return 2

  n+=1

  while 1:
     if IsPrime(n):return n
     if n%2==0:
        n+=1
     else:
        n+=2

def anp(n):

  #m=1015-n
  return next_prime(1015-n)

def fibo(n):

  if n==0: return 0 
  if n==1: return 1

  fprev1 = 1
  fprev2 = 0

  fibo = 0
  i=1
  while  i  < n:
    fibo = fprev1 + fprev2
    fprev2 = fprev1% 1300000000000
    fprev1 = fibo% 1300000000000
    i+=1

  return fibo% 1234567891011

   
def b(n):
  return fibo(anp(n))

if __name__ == "__main__":

  x = sum( b(i) for i in range(1,100000))

  print "The sum of b(n) for 1<=n<=100000 is", x%1234567891011

 

