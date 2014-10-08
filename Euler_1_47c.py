#
#  Find 3 consecutive 4 digit numbers composed of prime factors.
#


from Functions import IsPrime
from Values import prime_list

def pureFact(n):
  #print 'N:',n
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
 
  i = 1
  p = prime_list(i,True)
  #print p
  while p <= n:
    
    if n % p == 0:
      #print "!!",n,p
      n = n / p
      if not p in ilist:       
        numfacts += 1
        ilist.append(p)
        #print n, ilist 
    i+=1
    p = prime_list(i,True)
    #print p

  if numfacts==4:
     #print "#########"
     #print "n,Numfacts",n, numfacts
     return True
  else:
     return False
    

#print pureFact(644)
#print pureFact(645)
#print pureFact(646)

k = 0

#75486

for i in range (1000 , 100000):

    if pureFact(i): 
       print i, " contains 4 distinct prime factors"
       if pureFact(i+1):
         print "!!"
         if pureFact(i+2):
           print "!!!"
           if pureFact(i+3):
              print "!!!!!!!!!!!"
              k = i
              #print pureFact(i+1)
              #print pureFact(i+2)
              break
      

print "first factor of 4 is ",k
