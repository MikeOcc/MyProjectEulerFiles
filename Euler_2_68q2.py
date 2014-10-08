#
#
#  Euler problem 2-68
#


from itertools import combinations,permutations
from time import time
st = time()

#factors=[1,2,3,4,5,6,7,8,9,10]
factors = set(range(1,11))
factors2 = set(range(1,6))
#print factors

x = combinations(factors2,5)

ngon,u2,=[],[]
for z in x:
   #print "_________________"
   #print z
   u = list(factors.difference(z))
   #v = list(z); u = list(u)
   w = permutations(list(z))
   for t in w:
     #print t,u
     
     mvals=[]
     
     for i in xrange(4):
       mvals.append(t[0]+t[1]+u[i])
       
     for mv in mvals:
       utemp=[]
       isvalset= True  
       for i in xrange(5):
         val1 = t[i]+t[(i+1)%5]
         if not (mv-val1) in u:
           isvalset = False
           break
         else: 
           utemp.append(mv-val1)
           
       if len(set(utemp))!=5:
          isvalset=False
          break  #continue
       
       if isvalset == True:
          ngon.append(t);u2.append(tuple(utemp))  
          #print "Match!",t,utemp,mv
          #print

maxnum=0
for i in xrange(len(ngon)):
  ingon = ngon[i];outgon = u2[i]
  #print ingon, outgon

  x = min(outgon)

  #for strt, x in enumerate(outgon):
  #  break

  for k in xrange(5):
    if outgon[k]==x:
      strt = k
      break

  str1=""

  for k in xrange(strt,strt+5):
    str1 += str(outgon[k%5])+str(ingon[k%5])+str(ingon[(k+1)%5])
  #print str1

  if len(str1)==16:
    num = int(str1)
    if num>maxnum:maxnum=num


print 'The maximum 16-digit string for a "magic" 5-gon ring is',maxnum
print 'The process time is', time()-st



