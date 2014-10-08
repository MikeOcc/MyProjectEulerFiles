#
#
#
#

def Phi(Achnum,n,m,o,p,q,r,s):

  # Phi = Totient(n) 
  

  #Achnum = 2**n * 3**m * 5**o * 7**p * 11**q * 13**r
  
  #plist =[]

  powlist = (n,m,o,p,q,r,s)
  numlist = (1,2,4,5,10,12,16)
  divlist = (2,3,5,7,11,13,17)

  Phi = Achnum       #  start out with achilles # and then whittle down

  whittle = 1

  for i in range(0,7):      
       if powlist[i]>0: whittle *= numlist[i]

  Phi = Phi*whittle

  for i in range(0,7):       
       if powlist[i]>0: Phi /= divlist[i]
      

  #print "num = ",num,n,m,o

  return Phi

def IsPhiStrong(phi):

  if phi%2==0 and phi/4*4!=phi: return False

  if phi%3==0 and phi/9*9!=phi: return False

  if phi%5==0 and phi/25*25!=phi: return False

  if phi%7==0 and phi/49*49!=phi: return False

  if phi%11==0 and phi/121*121!=phi: return False

  if phi%13==0 and phi/169*169!=phi: return False

  if phi%17==0 and phi/289*289!=phi: return False

  return True


#-------------------------------------
from math import sqrt,pow,ceil

factlist = []
philist = []
Achlist = []


numstrong = 0

#for n in range(0,15):
#  for m in range(0,16):
#    for l in range (0,20):
#      for k in range(0,24):
#        for j in range(0,36):
#          for i in range (0,57):

#nthlist = []

#tel = {'jack': 4098, 'sape': 4139}

cutoff = 10**8  # 10**18  ##00

maxpower={0:0,1:0,2:0,3:0,4:0,5:0,6:0}

# Max Powers List is {0: 27, 1: 22, 2: 18, 3: 16, 4: 15, 5: 13, 6: 13}

bump =15

for o in range(0,14+bump):
 for n in range(0,14+bump):
   for m in range(0,15+bump):
     for l in range (0,16+bump):
       for k in range(0,18+bump):
         for j in range(0,226+bump):
           for i in range (0,28+bump):

            if i==1 or j==1 or k==1 or l==1 or m==1 or n==1 or o==1:continue
            if i==0 and j==0 and k==0 and l==0 and m==0 and n==0 and o==0:continue

           
           
            factlist=(i,j,k,l,m,n,o)
            chknum = 0
            for z in range(0,7):
               if factlist[z]>0:chknum += 1

            if chknum < 2: continue

            fact = (2**i) * (3**j) * (5**k) * (7**l) * (11**m) * (13**n) * (17**o)

            #print "fact =",fact,factlist

            if fact >= cutoff:continue 

            dontcont = False

            for nn in range(2,18):
              if round(fact**(1./nn),6) == int(round(fact**(1./nn),6)):
                #print "PERFECT!!",fact,  nn
                dontcont = True
                break

            if dontcont == True: continue

            #print "fact =",fact,factlist

            #factlist.append(fact)
            #factlist = list(set(factlist))

            phi = Phi(fact,i,j,k,l,m,n,o)
            #print "fact, phi: ", fact, phi,":",i,j,k,l,m,n,o

            dontcont = False

            for nn in range(2,18):
              if round(phi**(1./nn),6) == int(round(phi**(1./nn),6)):
                #print "PERFECT!!",phi,  nn
                dontcont = True
                break

            if dontcont == True: continue
    
            if IsPhiStrong(phi)==True:
              isStrong="Is Strong"
              numstrong += 1
              print
              print "Achilles #",fact, "of factors", i,j,k,l,m,n,o, " Phi(", fact ,")=", phi, isStrong
              Achlist.append(fact)

              for u in range(0,7):
                if factlist[u]> maxpower[u]:maxpower[u]=factlist[u]

            else:
              isStrong=""

 #   factlist.append(fact)
 #   philist.append(phi)

     #print "Achilles #",fact, "of factors", i,j,k,l,m,n, "Phi(", fact ,")=", phi, isStrong
     #print fact, i,j,k, phi, isStrong

#print factlist
#print philist

print "Numstrong", numstrong
xx = list(set(Achlist))
print "len Achlist", len(xx)
print "Number of strong integers below", cutoff, " is ", numstrong

print "Max Powers List is", maxpower
print "Bump is", bump

#flsort = sorted(factlist)

print
#print flsort

#flsort = sorted(factlist)