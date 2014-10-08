#
#  Euler Problem 92
#  []
#
from string import *
sum89=0

f89,f1=[89],[1]

for i in xrange(1,100):

  if i in f89 or i in f1:continue
  print "!!!",i
  temp,v=[],[]
  n=i
  #is89 = False

  while n!=1 and n!=89:
    x = list(str(n))
    print "XX",x
    tmp=0
    for z in x:
       tmp+=int(z)**2
    #print "tmp:",tmp

    if (tmp in f89):
      if len(temp)>0:
        for v in temp:
          f89.append(v)
      #temp=[]
      break
    elif (tmp in f1):
      if len(temp)>0:
        for v in temp:
          f1.append(v)       
      #temp=[]
      break
    else:
      temp.append(tmp)
    n=tmp

  if n==1:
    if len(temp)>0:
      for v in temp:
        f1.append(v) 
    f1.append(i)
  elif n==89:
    if len(temp)>0:
      for v in temp:
        f89.append(v)
    f89.append(i)

print "F1",f1   #sorted(f1)
print
print "F89",f89    #sorted(f89)
print
print "Answer is ",len(f89)
    
