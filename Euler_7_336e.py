#
#train = "FDABEC"      #"FAEBDC"
#train = "FDABEC"      #"FAEBDC"
#ord = "ABCDEF"
#train = "DACB"
#ord = "ABCD"
#train = "ABCDEF"      #"FAEBDC"
#

import itertools

def OrdTrain(train):

  ordmax = "ABCDEFGHIJKLMNOP"
  ord = ordmax[:len(train)]

  strlen = len(ord)

  numord = 0
  lexnum=0

  #if type(train) == 'str':
  llist = list(train)
  #else:
  #  llist = train

  print "!!!!", train, llist

  if list(ord) == llist: return 1

  #print "train",llist

  print llist
  print "****************"

  for numord in range(0,strlen):
    if llist[numord] != ord[numord]:       
       break


  matchfound = False

  while not matchfound:

     # search for next number to order
     srch = ord[numord]
     for j in range(0,strlen):
       if llist[j]==srch:
         srchnum = j
         break
     lexnum+=1
     print srchnum, llist[j]

     # find split point and rotate remainder
     if srchnum == strlen-1 and llist[srchnum]=="A":
       print"$%%$"
       llist = llist[::-1] 
     elif srchnum == strlen-1:
       #print "!!!"
       llist = llist[0:numord] + llist[:numord-1:-1]
     else: 
       llist = llist[0:srchnum] + llist[:srchnum-1:-1] 

     if llist == list(ord):

        print lexnum,")",llist
        matchfound = True
        print "matchfound!"
        break

     print lexnum,")",llist

     print "numord",numord, llist, ord

     if (numord<strlen) and (llist[numord] == ord[numord]):
       
        while numord<strlen and llist[numord] == ord[numord]:
          print "next match made", numord ,ord[numord],llist[numord]
          numord+=1
          if numord>=strlen:break
   
     if numord == 0: 
        llist =llist[::-1]
        #print llist
        lexnum+=1
        print lexnum,")",llist
     else:
 
        llist = llist[0:numord] + llist[:numord-1:-1]
        lexnum+=1
        print lexnum,")",llist

     print "lll", llist, list(ord)
     if llist == list(ord):
        matchfound = True
        print "QQ Matchfound!"
        break

    
     if (numord< strlen) and (llist[numord] == ord[numord]):
       
        while llist[numord] == ord[numord]:
          #print "next match made", numord ,ord[numord],llist[numord]
          numord+=1
       

  print "Trains Ordered! Total number of moves to order train is", lexnum
  print "__________________"

  return lexnum


if __name__ == "__main__":

  x=list(itertools.permutations(['A', 'B', 'C', 'D', 'E', 'F'],6))
  
  
  #OrdTrain(list("DFAECB"))
  #OrdTrain(list("ABCDFE"))
  #train = list("FDABEC")
   
  z = len(x)
  
  maxilist = []
  lexilist = []
  maxrotates = 0

  #for i in range(1,10):
  #  print i,")", list(x[i])

  #cc=""
  #for yy in x[20]:
  #  cc = cc + yy
  
  #print "CC", cc
  
  #print "!!!!!",x[6], type(x[6]), list(x[6])
  
  #OrdTrain(list(x[6]))

  for i in range(0,z):
    cc=""
    for yy in x[i]:
      cc = cc + yy
    cc = str(cc)
      # print x[i]
    xyzygy = OrdTrain(cc)
    maxilist.append(xyzygy)
    lexilist.append(cc)
    if xyzygy > maxrotates: maxrotates = xyzygy

  print "number of tries list", maxilist  
  print
  print "maximal number of moves in list is", maxrotates    
  











