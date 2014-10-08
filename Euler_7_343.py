#
#
#  Euler Problem 343
#



def f(n):
  n1=1.
  d1=n

  while 1:
    #if d1==n1:return 1
    n1+=1
    d1-=1
    #print n1,d1
    if d1!=n1 and d1/n1 == int(d1/n1):
      #print n1,d1,
      d1=d1/n1
      n1=1
      #print n1,d1
      #continue
    x = n1/d1
    if x==int(x):
      print "!",n,x
      return int(x)

summ=1
for k in xrange(2,101):
  summ+=f(k**1)

print "total is",summ


#print f(8 * 10**18)
# 2,6,12,6,30,42,18,72,12,36
# 1,2,1,4,2,6,1,2,4,10



