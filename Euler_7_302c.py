#
#  Euler 302 Strong Achilles numbers.. what a pain in the ass!
#
#

def Phi(Achnum,n1,m1,o1,p1,q1,r1,s1,t1,u1):

  # Phi = Totient(n) 
  

  #Achnum = 2**n1 * 3**m1 * 5**o1 * 7**p1 * 11**q1 * 13**r1 * 17**s1 * 19**t1 * 23**u1 
  
  #plist =[]

  powlist = (n1,m1,o1,p1,q1,r1,s1,t1,u1)
  numlist = (1,2,4,6,10,12,16,18,22)
  divlist = (2,3,5,7,11,13,17,19,23)

  Phi = Achnum       #  start out with achilles # and then whittle down

  whittle = 1

  for i in range(0,9):
     if powlist[i]>0: whittle *= numlist[i]

  Phi = Phi*whittle

  for i in range(0,9):
     if powlist[i]>0: Phi /= divlist[i]
      

  return Phi

def IsPhiStrong(phi):

  if phi%2==0 and (phi/4)*4!=phi: return False

  if phi%3==0 and (phi/9)*9!=phi: return False

  if phi%5==0 and (phi/25)*25!=phi: return False

  if phi%7==0 and (phi/49)*49!=phi: return False

  if phi%11==0 and (phi/121)*121!=phi: return False

  if phi%13==0 and (phi/169)*169!=phi: return False

  if phi%17==0 and (phi/289)*289!=phi: return False

  if phi%19==0 and (phi/361)*361!=phi: return False

  if phi%23==0 and (phi/529)*529!=phi: return False

  return True


#-------------------------------------
from math import sqrt,pow,ceil
from time import time



st = time()

factlist = []
philist = []
Achlist = []

numperfect=0

numstrong = 0

#for n in range(0,15):
#  for m in range(0,16):
#    for l in range (0,20):
#      for k in range(0,24):
#        for j in range(0,36):
#          for i in range (0,57):

#nthlist = []

#tel = {'jack': 4098, 'sape': 4139}

cutoff = 10**4  # 10**18  ##00
print
print
print "Processing hunt begins for Strong Achilles Numbers less than", cutoff
print

maxpower={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

# Max Powers List is {0: 27, 1: 22, 2: 18, 3: 16, 4: 15, 5: 13, 6: 0}

bump =0
  

for q in range(0,5):  #23
  if q==1:continue
  for p in range(0,5):  #19
    if p==1:continue
    for o in range(0,7):  #17
      if o==1:continue
      for n in range(0,7+bump):  #13
        if n==1:continue
        for m in range(0,7+bump):  #11
          if m==1:continue
          for l in range (0,8+bump):  #7
            if l==1:continue
            for k in range(0,13+bump):  #5
              if k==1:continue
              for j in range(0,23+bump):  #3
                if j==1:continue
                for i in range (0,25+bump):  #2
                    if i==1:continue

               #if i==1 or j==1 or k==1 or l==1 or m==1 or n==1 or o==1 or p==1:exit()
                    if i==0 and j==0 and k==0 and l==0 and m==0 and n==0 and o==0 and p==0 and q==0:continue
               
               
               
                    factlist=(i,j,k,l,m,n,o,p,q)
                    chknum = 0
                    #for z in range(0,8):
                    #  if factlist[z]>0:chknum += 1

                    #if chknum < 2: continue

                    fact = (2**i) * (3**j) * (5**k) * (7**l) * (11**m) * (13**n) * (17**o) * (19**p) * (23**q)

                    if fact >= cutoff:continue 

                    dontcont = False

                    for nn in range(2,20):    #18
                       #if round(fact**(1./nn),3) == int(round(fact**(1./nn),3)):
                       nroot = int(round(fact**(1./nn),5))
                       if nroot**nn == fact:
                         print "PERFECT!!",fact,nn,":",i,j,k,l,m,n,o,p,q,nroot**nn
                         numperfect+=1
                         dontcont = True
                         break

                    if dontcont == True: continue

                    phi = Phi(fact,i,j,k,l,m,n,o,p,q)
   
                    dontcont = False

                    #if round(phi**(.5),6) == int(round(phi**(.5),6)):continue

                    for nn in range(2,20):
                       #if round(phi**(1./nn),3) == int(round(phi**(1./nn),3)):
                       nroot = int(round(phi**(1./nn),5))
                       if nroot**nn == phi:
                          print "PERFECT!! skip it!",phi,nn,":",i,j,k,l,m,n,o,p,q,":", nroot**nn 
                          numperfect+=1
                          dontcont = True
                          break

                    if dontcont == True: continue
    
                    if IsPhiStrong(phi)==True:
                
                       numstrong += 1
                       print
                       print str(numstrong),") Strong Achilles #",fact, "of factors", i,j,k,l,m,n,o,p,q ," Phi(", fact ,")=", phi
                       #Achlist.append(fact)

                       for u in range(0,9):
                          if factlist[u]> maxpower[u]:maxpower[u]=factlist[u]
 

print    # "Numstrong", numstrong
#xx = list(set(Achlist))
#print   # "len Achlist", len(xx)
print "Number of strong integers below", cutoff, " is ", numstrong

print "Max Powers List is", maxpower
print "Bump is", bump
print "Number of perfect #s is", numperfect

#flsort = sorted(factlist)

print
print "Processing time is", time() - st
#print flsort

#flsort = sorted(factlist)

