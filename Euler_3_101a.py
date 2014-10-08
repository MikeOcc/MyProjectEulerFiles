#
#  Euler Problem 101
#
#

#from array import *

a=[];b=[];c=[];d=[];e=[];f=[];g=[];h=[];i=[];j=[];u=[]

for n in xrange(1,11):

  #u = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
  '''
  a.append(1) 
  b.append(682*n-681 )
  c.append(21461*n**2 + -63701*n +42241)
  d.append(1 - n + n**2 - n**3) 
  e.append(1 - n + n**2 - n**3 + n**4) 
  f.append(1 - n + n**2 - n**3 + n**4 - n**5) 
  g.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6) 
  h.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7) 
  i.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8) 
  j.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9) 
  '''
  u.append(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10)

print u

print 
print

summ = 0
for a in xrange(3,4):
   if a == 1: summ += 1;continue
   
   ar = [ [0 for col in range(a+2) ] for row in range(a)]
   for j in xrange(1,a+1):
     for i in xrange(1,a+1):
       ar[j-1][i-1] = (j)**(i-1)

     ar[j-1][i+1] = u[j-1]

   m=[]
   ctr=0
   print ar
   print
   for i in range(1,0,-1):
    for j in range(0,5):
      ar[i][j] = ar[i][j] -ar[i-1][j]

   for i in range(0,1):
    for j in range(0,5):
      ar[i][j] = ar[i][j] -ar[i-1][j]

   print ar

  