#
# Problem 188
#
#

def HyperExMod(a,b,c):
 
  a0=a;a00=a;b0=b
  
  for i in xrange(1,b):
     #print "I",i,"a",a
     a00=a0
     j=1;jmax=a
     #for j in xrange(1,a):
     while j<jmax:
        #print "J",j,"b",a
        a00=(a00*a0)%(10**c)
        a=a00
        j+=1

  return a00


print HyperExMod(3,3,8)