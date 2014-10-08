#
#  Euler Problem 41
#
#  find the largest n-digit pandigital prime

from Functions import IsPrime
from time import time




def SetMatch(n,nset):

  mset = set(str(n))
  
  yy = mset & nset

  if yy == mset and yy == nset: return True
  else:
    return False
 
st = time()

for i in range(123456,200000):
   
   sset = set(str(i))
   isfound = True
   ctr = 0
   for j in range(2,7):
     n = i * j
     if SetMatch(n,sset)== False :
        isfound = False
        break
     else:
        ctr += 1  
       # print "n:", i , j, n
       
     
   if isfound == True:   # and ctr =>4:   
     print "Answer found", i,i*2,i*3,i*4,i*5,i*6
     break
   else:
     continue
  

print "Process time is", time()-st