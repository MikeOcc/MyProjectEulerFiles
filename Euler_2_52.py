#
#
#
#
from Functions import IsPrime
from string import *
pset=[]

for i in range(56000,100000):

  if IsPrime(i):
    ii=str(i)
    jj=ii
    isdb=""
    hasdouble=False
    dig1=""
    mid=""
    if len(ii) > len(set(ii)):
       mid=ii[1:4]
       for k in range(0,len(mid)):
    
         if mid[k] in isdb:
           hasdouble=True
           dig1=dig1+mid[k]
         else:
           isdb+=mid[k] 
    
    if not hasdouble: continue
    
    dig1 = "".join(list(set(dig1)))
    
    if i==56003: print len(dig1),dig1[0]
    
    jj=ii[:2]+ii[-1:]

    #for m in range(0,len(dig1)):
    #     jj=jj.replace(dig1[m],'',2)
       
    print i,dig1,isdb,mid,jj

