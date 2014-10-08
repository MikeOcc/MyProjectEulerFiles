
train = "DBAC" #"DACB"

ord = "ABCD"
numord = 0
lexnum=0

llist = list(train)

print llist
print "****************"

for i in range(1,5):

   # search for next number to order
   srch = ord[numord]
   for j in range(0,4):
     if llist[j]==srch:
       srchnum = j
       break
   lexnum+=1
   #print srchnum, llist[j]

   # find split point and rotate remainder
   llist = llist[0:srchnum] + llist[:srchnum-1:-1] 

   print lexnum,")",llist
   
   if numord == 0: 
     llist =llist[::-1]
     #print llist
     lexnum+=1
     print lexnum,")",llist
   else:
     pass

   numord+=1


print "Total number of moves to order train is", lexnum

   
      
  











