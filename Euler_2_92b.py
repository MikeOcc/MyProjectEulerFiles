#
#  Euler Problem 92
#  []
#
from string import *
from mpmath import power
#print

f89,f1={89:1},{1:1}

for i in xrange(1,10**7+1):

  if i in f89 or i in f1:continue
  #print "!!!",i
  #temp,v=[],[]
  n=i
  temp,v=[],[]
  #is89 = False

  while n!=1 and n!=89:
    x = list(str(n))
   
    tmp=0
    for z in x:
       tmp+=int(power(int(z),2))
    

    if (tmp in f89):
      #print "*",
      #f89.append(i)
      f89[i]=1
      break
    elif (tmp in f1):
     
      #f1.append(i)
      f1[i]=1
      break

    n=tmp


print
#print "F1",f1   #sorted(f1)
print
#print "F89",f89    #sorted(f89)
print
print "Answer is ",len(f89),":",len(f1),";",float(len(f89))/float(len(f1))
    
