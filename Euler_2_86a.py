#
#
#  Euler Problem 86
#
#  []


def sp(a,b,c):

  r = sorted([a,b,c])

  mindy = ((r[2]**2 + (r[0]+r[1])**2)**.5)

  if int(mindy)==mindy:
    return 1

  return -1

###########

M=1850
MX=1000000

#print sp(3,5,6)
print "Calculating...."
ctr = 0
for i in xrange(1,M+2): 
  #print i,")",ctr
  if ctr>=MX:
     print ctr, i-1
     break
  for j in xrange(1,M+1):  
   for k in xrange(1,M+1):
     if i>=j>=k:
       if sp(i,j,k)>0:
         #print i,j,k
         ctr +=1

           

