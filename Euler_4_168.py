#
#
# Euler Prolem 168
#
#]



def f(n):

  ns = str(n)
  a = int(ns[-1:] + ns[:-1])

  d = float(a)/n

  if d==int(d):
    return int(d)
  else:
    return 0

zz= 1016949152542372881355932203389830508474576271186440677966
print zz < 10**100
print f(zz)
exit()

tot=0
for i in xrange(10,100000):
  x= f(i)
  if x:
    tot+=i
    print i,x,tot,str(tot)[-5:]

print "first set is",str(tot)[-5:]

print
tot1=0
for i in xrange(100000,1000000):
  x= f(i)
  if x>3:
    tot1+=i
    print i,x,tot1,str(tot1)[-5:]

print "2d set is",str(tot1)[-5:]

'''
print
tot2=0
for i in xrange(1000000,10000000):
  x= f(i)
  if x:
    tot2+=i
    print i,x,tot2,str(tot2)[-5:]

print "2d set is",str(tot2)[-5:]
'''

gtot = tot + 14*tot1 + 99995 * 94



print 
print "Answer is", str(gtot)[-5:]
  


