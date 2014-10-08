
#train = "FDABEC"      #"FAEBDC"

#train = "FDABEC"      #"FAEBDC"
#ord = "ABCDEF"

#train = "DACB"
#ord = "ABCD"

train = "BACDEF"      #"FAEBDC"
ord = "ABCDEF"

strlen = len(ord)

numord = 0
lexnum=0

llist = list(train)

print llist
print "****************"

matchfound = False

while not matchfound:

   # search for next number to order
   srch = ord[numord]
   for j in range(0,strlen):
     if llist[j]==srch:
       srchnum = j
       break
   lexnum+=1
   #print srchnum, llist[j]

   # find split point and rotate remainder
   if srchnum == strlen-1:
     #print "!!!"
     llist = llist[0:numord] + llist[:numord-1:-1]
   else: 
     llist = llist[0:srchnum] + llist[:srchnum-1:-1] 

   if llist == list(ord):

      print lexnum,")",llist
      matchfound = True
      break

   print lexnum,")",llist

   if llist[numord] == ord[numord]:
       
      while llist[numord] == ord[numord]:
        #print "next match made", numord ,ord[numord],llist[numord]
        numord+=1
   
   if numord == 0: 
      llist =llist[::-1]
      #print llist
      lexnum+=1
      print lexnum,")",llist
   else:

      llist = llist[0:numord] + llist[:numord-1:-1]
      lexnum+=1
      print lexnum,")",llist

   if llist == list(ord):
      matchfound = True
      break

    
   if llist[numord] == ord[numord]:
       
      while llist[numord] == ord[numord]:
        #print "next match made", numord ,ord[numord],llist[numord]
        numord+=1
       

print "Trains Ordered! Total number of moves to order train is", lexnum

   
      
  











