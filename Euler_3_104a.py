#
#  Euler Problem 104
#
#

def IsPan(s):
  
  return "".join(sorted(s))=='123456789'

###########
from time import time
st=time()
F1b, F2b, F1e, F2e = 1,1,1,1

#y=(2**38-1)

for i in xrange(21112749-2):
   
   if F1b>10**16:
     #print "!",F1b
     F1b=int(float(F1b)/100.)
     F2b=int(float(F2b)/100.)
     #print F1b,F2b

   if F1e>10**12:
     F1e=int(str(F1e)[-11:])
     F2e=int(str(F2e)[-11:])
     
   Fb = F2b + F1b
   F1b = F2b
   F2b = Fb
   
   Fe = F2e + F1e
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


  