#
#The number, 1406357289, is a 0 to 9 pandigital #number because it is made up of each of the #digits 0 to 9 in some order, but it also has a #rather interesting sub-string divisibility #property.
#
#Find the sum of all 0 to 9 pandigital numbers with this property.
#

def PanDig(n):

  nset = set(str(n))
  lnset = len(nset)

  for m in xrange(1,lnset):
    if str(m) not in nset: return False

  return True

def MultDig(n,exchunk="0"):
  #print "n",n
  nset = str(n)
  lnset = len(nset)

  if lnset==2:
    nset="0"+nset
    lnset==3

  
  chklst = [0]*10
  
  for z in xrange(lnset):

    if nset[z] in exchunk:
       #print nset[z],exchunk
       return False
    if chklst[int(nset[z])]==0:
       chklst[int(nset[z])]=1
    else:
       return False
  return True

if __name__ == '__main__':

  from time import time
  st = time()

  pandigs = []  # list of pandigital numbers with special property


# gen fist chuncks
  for i in xrange(12,988):
      if i%17==0 and MultDig(i):
         #print i
         chunk1 = str(i)
         for j in xrange(12,988):
            
            if j%7==0 and MultDig(j,chunk1):
             # print j, str(j) + str(i)
          
              chunk2 = str(j) + str(i)
              for k in xrange(12,988):
            
                if k%2==0 and MultDig(k,chunk2):
                  chunk3 = str(k) + str(j) + str(i)
                  for l in xrange(10):
                    if str(l) not in chunk3:
                       chunk3 = str(l) + chunk3
                       break
                  #print chunk3
                  if int(chunk3[2:5])%3==0 and int(chunk3[3:6])%5==0 and int(chunk3[5:8])%11==0 and int(chunk3[6:9])%13==0:                   
                    pandigs.append(chunk3)

  pandigs.sort()
  print pandigs
  print
  print "The sum of all Pandigital #s with this property is ", sum(int(i) for i in pandigs)
  print "Process time is",time()-st





