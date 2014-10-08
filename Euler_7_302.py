#
#
#
#

def Phi(n,m,o,p,q,r):

  #print "n,m,o",n,m,o

  num = 2**n * 3**m * 5**o * 7**p * 11**q * 13**r
  num1 = 1;div1=2
  num2 = 2;div2=3
  num3 = 4;div3=5
  num4 = 1;div1=7
  num5 = 2;div2=11
  num6 = 4;div3=13
  
  #print "num = ",num,n,m,o

  if o==0:
    num = 2**n * 3**m
    resu = int(round(float(num) * (1./2.)*(2./3.),3))  # num*num2/div1/div2    

  elif m==0:
    num = 2**n * 5**o
    #print num, n,m,o
    resu = int(round(float(num) * (1./2.)*(4./5.),3)) #((num*num3)/div1)/div3

  elif n==0:
    num = 3**m * 5**o
    resu = int(round(float(num) * (2./3.)*(4./5.),3))  #((num*num2*num3)/div1)/div3


  elif p==0:
    num = 3**m * 5**o
    resu = int(round(float(num) * (2./3.)*(4./5.),3))  #((num*num2*num3)/div1)/div3

  elif q==0:
    num = 3**m * 5**o
    resu = int(round(float(num) * (2./3.)*(4./5.),3))  #((num*num2*num3)/div1)/div3

  elif r==0:
    num = 3**m * 5**o
    resu = int(round(float(num) * (2./3.)*(4./5.),3))  #((num*num2*num3)/div1)/div3

  else:
    num = 2**n * 3**m * 5**o
    #print "!!!",num,":",num1,num2,num3,div1,div2,div3
    #resu = num*num2*num3/div1/div2/div3
    resu = int(float(num)*float(num2)*float(num3)/float(div1)/float(div2)/float(div3))


  return resu

def IsPhiStrong(phi,m,n,o,p,q,r):

  if m!=0 and m>1 and phi/4*4!=phi: return False
  if n!=0 and n>1 and phi/9*9!=phi: return False
  if o!=0 and o>1 and phi/25*25!=phi: return False
  if p!=0 and p>1 and phi/49*49!=phi: return False
  if q!=0 and q>1 and phi/121*121!=phi: return False
  if r!=0 and r>1 and phi/169*169!=phi: return False
  return True


#-------------------------------------
from math import sqrt,pow,ceil

factlist = []
philist = []

cutoff = 10**18  ##00
numstrong = 0
# 13: 15,16
# 11: 16,17
#  7: 20,21
#  5: 24,25
#  3: 36, 37
#  2: 57,58
#
for i in range (0,57,):
  for j in range(0,36):
   for k in range(0,24):
     for l in range (0,20):
       for m in range(0,16):
         for n in range(0,15):
 
           if i==0 and j==0 and k==0:continue

           if (i==0 and j==0) or (j==0 and k==0) or (i==0 and k==0):continue

           if i==1 or j==1 or k==1 or l==1 or m==1 or n==1:continue

           fact = (2**i) * (3**j) * (5**k) * (7**i) * (11**j) * (13**k)
           #print "fact =",fact

           if fact > cutoff-1:continue 

           dontcont = False

           for nn in range(2,14):
             if ceil(round(fact**(1./nn),3)) == int(fact**(1./nn)):
               #print "PERFECT!!",fact,  nn
               dontcont = True
               break

           if dontcont == True: continue

           #factlist.append(fact)
           #factlist = list(set(factlist))

           phi = Phi(i,j,k,l,m,n)
           #print "fact, phi: ", fact, phi
    
           if IsPhiStrong(phi,i,j,k,l,m,n)==True:
             isStrong="Is Strong"
             numstrong += 1
             print
             print "Achilles #",fact, "of factors", i,j,k,l,m,n "Phi(", fact ,")=", phi, isStrong

           else:
             isStrong=""

 #   factlist.append(fact)
 #   philist.append(phi)

    #print "Achilles #",fact, "of factors", i,j,k, "Phi(", fact ,")=", phi, isStrong
    #print fact, i,j,k, phi, isStrong

#print factlist
#print philist


print "Number of strong integers below", cutoff, " is ", numstrong

#flsort = sorted(factlist)

print
print flsort

#flsort = sorted(factlist)