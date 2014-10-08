#
#
#
#

def Phi(n,m,o,p,q,r):

  # Phi = Totient(n) 
  #print "n,m,o",n,m,o

  Achnum = 2**n * 3**m * 5**o * 7**p * 11**q * 13**r
  #num1 = 1;div1=2
  #num2 = 2;div2=3
  #num3 = 4;div3=5
  #num4 = 6;div1=7
  #num5 = 10;div2=11
  #num6 = 12;div3=13
  
  #plist =[]

  powlist = (n,m,o,p,q,r)
  numlist = (1,2,4,5,10,12)
  divlist = (2,3,5,7,11,13)

  Phi = Achnum       #  start out with achilles # and then whittle down

  whittle = 1

  for i in range(0,6):      
       if powlist[i]>0: whittle *= numlist[i]

  Phi = Phi*whittle

  for i in range(0,6):       
       if powlist[i]>0: Phi /= divlist[i]
      

  #print "num = ",num,n,m,o

  return Phi

def IsPhiStrong(phi,m,n,o,p,q,r):

 # print "!!!",phi,m,n,o,p,q,r

#  if m!=0 and m>1 and phi/4*4!=phi: return False
#  if n!=0 and n>1 and phi/9*9!=phi: return False
#  if o!=0 and o>1 and phi/25*25!=phi: return False
#  if p!=0 and p>1 and phi/49*49!=phi: return False
#  if q!=0 and q>1 and phi/121*121!=phi: return False
#  if r!=0 and r>1 and phi/169*169!=phi: return False

  #print "Fail 1", phi/4*4!=phi
  if m!=0 and m>1 and phi/4*4!=phi: return False
  #print "Fail 2", phi/9*9!=phi
  if n!=0 and n>1 and phi/9*9!=phi: return False
  #print "Fail 3", phi/25*25!=phi
  if o!=0 and o>1 and phi/25*25!=phi: return False
  #print "Fail 4", phi/49*49!=phi
  if p!=0 and p>1 and phi/49*49!=phi: return False
  #print "Fail 5"
  if q!=0 and q>1 and phi/121*121!=phi: return False
  #print "Fail 6"
  if r!=0 and r>1 and phi/169*169!=phi: return False

  return True


#-------------------------------------
from math import sqrt,pow,ceil

factlist = []
philist = []
Achlist = []

cutoff = 10**4  # 10**18  ##00
numstrong = 0
# 13: 15,16
# 11: 16,17
#  7: 20,21
#  5: 24,25
#  3: 36, 37
#  2: 57,58
#
#for i in range (0,57,):
#  for j in range(0,36):
#   for k in range(0,24):
#     for l in range (0,20):
#       for m in range(0,16):
#         for n in range(0,15):

#for n in range(0,15):
#  for m in range(0,16):
#    for l in range (0,20):
#      for k in range(0,24):
#        for j in range(0,36):
#          for i in range (0,57):

#nthlist = []

for n in range(0,2):
  for m in range(0,2):
    for l in range (0,20):
      for k in range(0,24):
        for j in range(0,36):
          for i in range (0,57):

           if i==1 or j==1 or k==1 or l==1 or m==1 or n==1:continue
           if i==0 and j==0 and k==0 and l==0 and m==0 and n==0:continue

           #if (i==0 and j==0) or (j==0 and k==0) or (i==0 and k==0):continue
           
           factlist=(i,j,k,l,m,n)
           chknum = 0
           for z in range(0,6):
              if factlist[z]>0:chknum += 1

           if chknum < 2: continue

           fact = (2**i) * (3**j) * (5**k) * (7**l) * (11**m) * (13**n)

           #print "fact =",fact,factlist

           if fact >= cutoff:continue 

           dontcont = False

           for nn in range(2,14):
             if round(fact**(1./nn),6) == int(round(fact**(1./nn),6)):
               #print "PERFECT!!",fact,  nn
               dontcont = True
               break

           if dontcont == True: continue

           #print "fact =",fact,factlist

           #factlist.append(fact)
           #factlist = list(set(factlist))

           phi = Phi(i,j,k,l,m,n)
           #print "fact, phi: ", fact, phi,":",i,j,k,l,m,n

           dontcont = False

           for nn in range(2,14):
             if round(phi**(1./nn),6) == int(round(phi**(1./nn),6)):
               #print "PERFECT!!",phi,  nn
               dontcont = True
               break

           if dontcont == True: continue
    
           if IsPhiStrong(phi,i,j,k,l,m,n)==True:
             isStrong="Is Strong"
             numstrong += 1
             print
             print "Achilles #",fact, "of factors", i,j,k,l,m,n, ", Phi(", fact ,")=", phi, isStrong
             Achlist.append(fact)

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

#flsort = sorted(factlist)

print
#print flsort

#flsort = sorted(factlist)