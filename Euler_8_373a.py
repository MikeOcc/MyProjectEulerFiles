from time import time

def r(a,b,c):
  #print a,b,c
  x=(a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)
  if x<=0:return -1
  r = a*b*c/(x)**.5
  return r

st = time()
summ = 0

lim = 1*10**2

for i in xrange(10,2*lim+1,2):
  for j in xrange(2*lim,0,-2):
    fnd = False
    for k in xrange(6,i+j,2):
    
       if i<j or j< k:continue
       R = r(i,j,k)

       if R>0 and R <= lim and R == int(R):
         summ +=R
         print "R",":",i,j,k,":",R,"/",float(i/R)
         fnd = True
         break

print summ
print "process time", time()-st