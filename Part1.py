
from Euler_Prime import IsPrime
import time
#y=[]

factlist = [0]

for i in range (0,11):
  for j in range(0,11):

    fact = 2**i * 3**j
    factlist.append(fact)
    print i,j, fact


flsort = sorted(factlist)
print
print factlist
print
print flsort

#exit()

sum = 0
sumtofind = 233
numfinds = 0
sumofprimes = 5    #  Start at 5 since algorithm misses sole single factors, 2^1*3^0;2^0*3^1
numofprimes = 2
cursum = 0
starttime = time.time()


xp=0;yp=0;zp=0;wp=0

MaxPrime = 200
StartPrime = 100

howdeep = 25

print "Beginning sum of Primes=q such that P(q) =",MaxPrime

print type(flsort)



for s in range(StartPrime , MaxPrime):
  
  

  if IsPrime(s):
     sumtofind = s
     print "for prime = ",s
  else:
     sumtofind = 0
     continue
  prevd = 0
  howdeep = 0
  for d in flsort:
    howdeep = howdeep + 1
    howdeep2 = d
    #print howdeep2
    if howdeep2 > s:
      #howdeep = prevd
      break
    #else:
        
  
  howdeep += 2
  
  #print "howdeep = ",howdeep,s
  #continue
  
  #print
  #print "Prime is", sumtofind,"_____________________________________"
  numfinds = 0


  for k in range(2, howdeep):
    for l in range(2, howdeep):
      for m in range(0, howdeep):
       for n in range(0, howdeep):

          #if m==1 or n==1: continue
          #print "KLM", k, l, m,s,sumtofind
          w= flsort[k]
          x= flsort[l] 
          y= flsort[m] 
          z= flsort[n]
           
          sum = w+x+y+z
        
          #if x==9 and y==8 and z==0 and sumtofind==17:  
          #   print "BAM!",x,y,z,"Sum = ",sum
          #   print (x>y>z) and(y!=0 and (x/y*y!=x)) and (z!=0 and (x/z*z!=x)) and (z!=0 and (y/z*z!=y))
          #   print "EndBame"

          if sum == sumtofind:
             if y ==0 and z==0 :
               ncf = (w/x*x!=w)
             elif z==0:
               ncf = ((w/x*x!=w) and (w/y*y!=w) and (x/y*y!=x))
             elif y==0:
               ncf = ((w/x*x!=w) and (w/z*z!=w) and (x/z*z!=x))
             else:
               ncf = ((w/x*x!=w) and (w/y*y!=w) and (w/z*z!=w) and (x/y*y!=x) and (x/z*z!=x) and (y/z*z!=y))
               #(y!=0 and (x/y*y!=x)) and (z!=0 and (x/z*z!=x)) and (z!=0 and (y/z*z!=y))


           
             if ((z==0 and w>x>y) or (w>x>y>z)) and ncf: 
               if numfinds >1:break
               numfinds += 1
               cursum = sum
               #print "Prime is ", sum, "Facts", w,x,y,z, numfinds
               if numfinds == 1:
                  wp=w;xp=x;yp=y;zp=z
    
  #print
  #print "Prime is", sumtofind
  if numfinds ==1:
      sumofprimes += s 
      numofprimes += 1          
      print "Hit!"
      print "Factors for ",sumtofind,":",wp,xp,yp,zp,cursum
  elif numfinds > 1:
      print "MultiHit!"
      print wp,xp,yp,zp,numfinds,cursum      

print
print "Sum of Primes for q< 100 is ", sumofprimes, ": Number of Primes", numofprimes 
print "Process took",time.time()-starttime,"seconds"


