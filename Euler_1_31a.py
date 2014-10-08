#
# Euler 31
#
#
from itertools import *

#print list(product([200,100,50,20,10,5,2,1] , repeat = 200))


cur = [100, 50, 20, 10,  5,   2,   1]
fac = [  2,  4, 10, 20, 40, 100, 200]

val = 200
ctr = 8
cntdown = 8

cnt = 200
for i in range(0,2):
   cnt-=i*cur[0]
   print cnt,cur[0]
   if cnt == 0:
       cnt = 200
       ctr += 1;print ctr
       break
   print "Level 1:"
   for j in range(0,4):
     if cnt == 0:break
     print cnt,cur[1]
     cnt-=j*cur[1]
     if cnt == 0:
         cnt = 200
         ctr += 1;print ctr
         break
     print "Level 2:"   
     for k in range(0,11):  
      if cnt == 0:break
       
      cnt-=k*cur[2]
      print cnt,cur[0]
      if cnt == 0:
         cnt = 200
         ctr += 1;print ctr
         break
         print "Level 3:"
         for l in range(0,21): 
           if cnt == 0:break
           cnt-=l*cur[3]
           if cnt == 0:
            cnt = 200
            ctr += 1;print ctr
            break
         print "Level 4:"
         for m in range(1,41):
           if cnt == 0:break
           cnt-=m*cur[4]
           print cnt,cur[0]
           if cnt == 0:
            ctr += 1;print ctr
            break
           print "Level 5:"
           for n in range(0,101):
             if cnt == 0:break
             
             cnt-=n*cur[5]
             print cnt,cur[5]
             if cnt == 0:
               cnt = 200
               ctr += 1;print ctr
               break
             print "Level 6:"
             for o in range(0,201):
               if cnt == 0:break
               cnt-=o*cur[6]
               print cnt,cur[6]
               if cnt == 0:
                 cnt = 200
                 ctr += 1;print ctr
                 break

print "total number of permutations is " , ctr


