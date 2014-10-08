#
#
#  Euler 340
#
import sys

sys.setrecursionlimit(7000)
global a,b,c
a=50;b=2000;c=40
#a=21**7%10**9;b=7**21%10**9;c=12**7%10**9

def F(n):
    print "n",n
    print "ab",a,b,c
    print "!",type(n)
    if n> b:

      print "made it"
      print n
      print n-c
      return n - c
      
    else: 
      
      print "recursing"
      F(a + F(a + F(a + F(a+n))))
      #return 4*a + n
      
print F(0)

exit()

def S(d,e,f):
  global a,b,c
  a= d;b=e;c=f
  a=50;b=2000;c=40
  summ = 0

  for i in range(0,b+1):
      summ += F(i)

print S(50,b,c)

   