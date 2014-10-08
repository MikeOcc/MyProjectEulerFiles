

def r(a,b,c):
  #print a,b,c
  x=(a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)
  if x<=0:return -1
  r = a*b*c/(x)**.5
  return r


summ = 0

for i in xrange(10,2401,2):
  for j in xrange(1,2401):
    for k in xrange(1,i+j):
       if i<j or j< k:continue
       R = r(i,j,k)

       if R>0 and R < 1201 and R == int(R):
         summ +=R
         print "R",":",i,j,k,R

print summ