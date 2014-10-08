#
#  Find 3 consecutive 4 digit numbers composed of prime factors.
#


from Functions import IsPrime
from time import time



def pureFact(n):

  ilist =  []
  
  numfacts = 0
  nstr = str(n)

  n0 = n

  if n % 2 == 0: 
    numfacts += 1
    ilist.append(2)
    n = n/2
    #ilist[0] = 1
    #print n, list
  
  
  #for i in range(3,int((n/30.))+1,2):
 
  i = 3
  while i <= n:   
 
    if IsPrime(i) == False: 
      i+=2
      continue    
    #if i == n: break
    if n % i == 0:
      n = n / i
      if not i in ilist:       
        numfacts += 1
        ilist.append(i)
        #print n, ilist  
    i+=2  

  if numfacts==4:
     #print "#########"
     #print "n,Numfacts",n, numfacts
     return True
  else:
     return False
    

#print pureFact(644)
#print pureFact(645)
#print pureFact(646)

if __name__ == '__main__':

  st = time()

  k = 0

  for i in xrange (100000 , 1000000):

      if pureFact(i): 
         #print i, " contains 4 distinct prime factors"
         if pureFact(i+1):
           #print "!!"
           if pureFact(i+2):
             #print "!!!"
             if pureFact(i+3):
                print "!!!!!!!!!!!"
                k = i
                #print pureFact(i+1)
                #print pureFact(i+2)
                print i, " contains 4 distinct prime factors"
                break
      

  print "first factor of 4 is ",k
  print "process time is ", time() - st