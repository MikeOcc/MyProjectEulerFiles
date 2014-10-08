#
#  Euler problem 336
#
#

import itertools

def OrdTrain(train,lexiconum):

  ordmax = "ABCDEFGHIJKLMNOP"
  ord = ordmax[:len(train)]

  strlen = len(ord)

  numord = 0
  lexnum=0


  llist = list(train)

  #print lexiconum,")!!!! Order Trains", llist

  if list(ord) == llist: return 1

  #print "****************"

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
    # print srchnum, llist[j]

     # find split point and rotate remainder
     if srchnum == strlen-1 and llist[srchnum]=="A":
     #  print"$%%$"
       llist = llist[::-1] 
     elif srchnum == strlen-1:
       #print "!!!"
       llist = llist[0:numord] + llist[:numord-1:-1]
     else: 
       llist = llist[0:srchnum] + llist[:srchnum-1:-1] 

     if llist == list(ord):

        ##print lexnum,")",llist
        matchfound = True
        ##print "matchfound!"
        break

     #print lexnum,")",llist

    # print "numord",numord, llist, ord

     if (numord<strlen) and (llist[numord] == ord[numord]):
       
        """
        while llist[numord] == ord[numord]:
          print "next match made", numord ,ord[numord],llist[numord]
          numord+=1
          if numord>=strlen:break
        """
        for v in range(numord,strlen):
          if ord[v] != llist[v]:
            #print "nnnext match made", numord,v,ord[v],llist[v]
            break
          #else:
            #print "nnext match made", numord,v,ord[v],llist[v]
        numord = v
       # srch = ord[numord]
       # for j in range(0,strlen):
       #   if llist[j]==srch:
       #     numord = j
       #     break  
       

     if numord == 0: 
        llist =llist[::-1]
        #print llist
        lexnum+=1
        #print lexnum,")",llist
     else:
        """ 
        llist = llist[0:numord] + llist[:numord-1:-1]
        lexnum+=1
        print lexnum,")",llist
        """
     #print "lll", llist, list(ord)
     if llist == list(ord):
        matchfound = True
      #  print "QQ Matchfound!"
        break

    
     if (numord< strlen) and (llist[numord] == ord[numord]):
       
        while llist[numord] == ord[numord]:
          #print "next match made", numord ,ord[numord],llist[numord]
          numord+=1
       

  #print "Trains Ordered! Total number of moves to order train is", lexnum
  #print "__________________"

  return lexnum



def permutations(li):


  if len(li) <= 1:
    yield li
  else:
    for el in li:
      for p in permutations([e for e in li if not e == el]):
        yield [el] + p


if __name__ == "__main__":

 # x=list(itertools.permutations(['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K'],11))
  
  
  #OrdTrain(list("DFAECB"))
  #OrdTrain(list("ABCDFE"))
  #train = list("FDABEC")
   
  #z = len(x)
  
  maxilist = []
  lexilist = []
  maxrotates = 0

  #x=list( "ABCDEFGHIJK")
  
  #x=list( "ABCDEF")
  x=list( "ABCDEFGHIJK")

  i=0
  j=0
  
  for p in permutations(x):

    i+=1
 
    xyzygy = OrdTrain(p,i)
    maxilist.append(xyzygy)
    #lexilist.append(cc)
    if xyzygy > maxrotates: 
       maxrotates = xyzygy
       lexilist = []
       lexilist.append(p)
       j=1
       print "New increase in maxrotates:",maxrotates
    elif xyzygy == maxrotates:
       lexilist.append(p)
       j+=1
    
    if j==2011:
      print "The 2011th Lexigraphic number is ",str(lexilist[j-1])
    
  #print "number of tries list", maxilist  
  print
  print "maximal number of moves in list is", maxrotates    
  print
  print "number of maximix arrangements is", len(lexilist)
  print
  ctr=0
  for k in lexilist:  
    ctr+=1
    #print ctr,") ",str(k)


    if j==2011:
      print "The 2011th Lexigraphic number is ",str(lexilist[j-1])
      












