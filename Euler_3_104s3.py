PAND=set('123456789') 
TAIL=1000000000 
HEAD=10000000000000000 

def pandigital(x): 
  return set(x) == PAND 

from time import time
st=time()

c=2 
a=b=aa=bb=1 
for i in range(10000000): 
   a = a+b 
   b = a-b 
   a %= TAIL 
   b %= TAIL 

   aa = aa+bb 
   bb = aa-bb 

   if(aa > HEAD and bb > HEAD): 
     aa/=10 
     bb/=10 

   c += 1 
   if( pandigital(str(a)) and pandigital(str(aa)[0:9])): 
    print c 
    break 


print "process time is",time()-st
assert(c==329468) 