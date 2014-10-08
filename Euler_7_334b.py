#
#
#
# 63D547B16C
#

from math import floor

t={} 
b={} 

t[0]=123456 

b[1]=289
b[2]=145

noBM1 = True
ctr=1
begin1 = 217
end1=218


for i in range( 1 , 1501):

  if i%2==0:
     t[i]=t[i-1]/2
  else:
     t[i]=int(floor((t[i-1]/2)))^926252

  b[i]=(t[i-1]/2)%2048 + 1

  #print i,t[i],t[i-1],b[i] 
  
for i,j in b.iteritems():
  print i,j

exit()

while ctr<434:
  
  for j in range(1,ctr+1):
     
     print "!!",b[j]
     if b[j]<2:
     #  j+= j%434
       continue 
     try:
       if b[j]>1:
         b[j-1]=b[j-1]+1
         b[j]-=1
     except KeyError:
       b[j-1]=1

     try:
       if b[j]>0:
         b[j+1]=b[j+1]+1
         b[j]-=1
     except KeyError:
       b[j+1]=1

     
 
     print"#------------"
     print ctr, j, 
     for j in range(1,ctr-1):
       print j, b[j],
     ctr+=1
     print

     #if begin1>-1:begin1-=1
     #if end1>435 : end1=+1



        






