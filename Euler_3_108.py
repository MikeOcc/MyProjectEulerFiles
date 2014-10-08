#
#
#
#  x + y = xy/n
#
#  1/x = 1/n - 1/y
#  
#
#

n = 235620 #500000000

x = 1
y = 1
ctr=0
if n%2==0:
  m=n/2
else:
  m=(n/2)-1

'''
for x in xrange(n*2,0,-1):
  for y in xrange(n*2,300000):
    if y>=x:
      if n*(x+y) == x*y:
        print x,y
        ctr +=1
'''

for x in xrange(n*2,n,-1):
      if n==x:continue
      y = float(n*x)/(x-n )
      #if int(y) == y:
      if int(y)==y:
        print x,y
        ctr +=1

print
print "# of solutions for",n, "is", ctr

     






