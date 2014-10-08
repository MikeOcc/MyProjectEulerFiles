#
#  Euler Problem 24
#  Find Millionth Lexicographic perm of
#  digits 0-9
#


def makenum(dignum):

  retnum = ""
  for i in range(0,10):
    retnum += str(dignum[i])
  return int(retnum)

################################

def nodouble(n):

  #nodoub = True
  checkstr = [0,0,0,0,0,0,0,0,0,0]
  retval = 1 
  x = str(n)
  if len(x)<10:x="0"+x

  #print x
  zz=len(x)-1
  for j in range(zz,-1,-1):     #xrange(len(x)):
    val = int(x[j])
    if checkstr[val]!=-1:
      if val == 9:
        #print "boo!", val, j
        retval = j
      checkstr[val]=-1
    else:
      #nodoub=False
      #break
      retval= -2
      break

  return retval

###################################
from time import time

starttime = time()
       
ctr=0
#basedig = [0,1,2,3,4,5,6,7,8,9]
#curdig = [0,1,2,3,4,5,6,7,8,9]

i=123456788
prev=i
prevchkval = 9

while i<9999999999L:  #1234567890)
   
  i+=1
  checkval = nodouble(i)
  if(checkval != -2):
    diff = i-prev
    diffchk=checkval-prevchkval
    ctr +=1
    
    #print ctr,")", i, diff, checkval, diffchk
    prev = i
    prevchkval = checkval
    i+=8
    

  if ctr == 1000000:  #   0000:
    print "YES!!!!!", i-8
    break



print "1000000th Lexicographic perm is " ,i-8
print "Process took ", time()-starttime,"seconds"