#
#  Find 3 consecutive 4 digit numbers composed of prime factors.
#


from Functions import IsPrime

def pureFact(n):

  ilist =  []
  
  numfacts = 0
  nstr = str(n)

  if n % 2 == 0: 
    numfacts += 1
    ilist.append(2)
    #ilist[0] = 1
    #print n, list
  
  
  for i in range(3,int(n/2)+1,2):
  
    if IsPrime(i) == False: continue    

    if n % i == 0:

      if not i in ilist:       
        numfacts += 1
        ilist.append(i)
        #print n, ilist  
  
  if numfacts>=4:
     #print "#########"
     #print "n,Numfacts",n, numfacts
     return True
  else:
     return False
    

#print pureFact(644)
#print pureFact(645)
#print pureFact(646)

k = 0

for i in range (20000 , 30000):

    if pureFact(i): 
       if pureFact(i+1) and pureFact(i+2) and pureFact(i+3):
          print "!!!!!!!!!!!"
          k = i
          #print pureFact(i+1)
          #print pureFact(i+2)
          break
      

print "first factor of 4 is ",k
