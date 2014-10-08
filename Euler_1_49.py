#
#  Euler 49
#
#


from itertools import *
from Functions import IsPrime


for i in range(1000,3000):

  if IsPrime(i) and i != 1487 and i != 1847:

    ilist = list(set(list(permutations(str(i)))))
    #ilist = list(permutations(str(i)))



    #ilist = int("".join(ilist))

    plist = []

    for k in xrange(len(ilist)):
       x= int("".join(ilist[k]))
       if x>999 and IsPrime(x): 
         plist.append(x)
         #print x
    
    
    if len(plist) >2 or not (1487 in plist):
       plist.sort()
       #print "Prime List",i,")",plist
       #print type(plist[0]), len(plist)
       dlist =[]
       for u in plist:
         for v in plist:
            if v>u and v-u>1000:
              dlist.append(v-u)
       dlist.sort()
       
       prev = 0
       dblist=[]
       for l in range(1,len(dlist)):
         if dlist[l]==dlist[l-1]:
           dblist.append(dlist[l])
           #print "Double Value Found!!!",dlist[l]
       if len(dlist)>0:
         for m in range(0,len(dblist)):
           if 2 * dblist[m] in dlist:
             print "Eureka!",dblist[m]
             print "Prime List:",plist
             print "Answer is",str(plist[1])+str(plist[2])+str(plist[3])
       










    
