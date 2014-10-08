#
#  Euler Problem 104
#
#

def IsPan(s):
  #return set(s) == set('123456789')
  #return "".join(sorted(s))=='123456789'
  return ("1" in s and "2" in s and "3" in s and
            "4" in s and "5" in s and "6" in s and
            "7" in s and "8" in s and "9" in s)

###########
from time import time
st=time()
F1b, F2b, F1e, F2e = 1,1,1,1

#y=(2**38-1)

for i in xrange(21112749-2):
   
   if F1b>10**16:
     #print "!",F1b
     F1b/=1000
     F2b/=1000
     #print F1b,F2b

   #if F1e>10**12:
   #  F1e=int(str(F1e)[-11:])
   #  F2e=int(str(F2e)[-11:])
     
   Fb = F2b + F1b
   F1b = F2b
   F2b = Fb
   
   Fe = (F2e + F1e)%1000000000
   F1e = F2e
   F2e = Fe
   

   Fstrb = str(Fb)[:9]
   
   if IsPan(Fstrb):
     Fstre = str(Fe)[-9:]
     if IsPan(Fstre): 
       print "k is", i+3
     
       break


print Fb
#print i+3,F
print Fstrb,Fstre
print "Process time is", time()-st


  