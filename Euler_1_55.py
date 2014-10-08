from Functions import IsPalindrome,RevNumber
from Euler_Prime import IsPrime

numLychrel = 0
numPalLychrels = 0

numint = 100001

for i in range(1,numint):

  L = i
  FisP = IsPalindrome(L)

  for j in range(1,51):
    IsFound = False
    RN = RevNumber(L)
    LR = L + RN
    IsPal = IsPalindrome(LR)
    if IsPal == True:
      IsFound = True
      break
    else:
      L = LR
  if IsFound == False:
    numLychrel +=1
    if IsPrime(i):
      Isp = "...Prime!"
    else:
      Isp = ""
    PalLyc = ""
    if FisP:
      numPalLychrels+=1
      PalLyc = "...Palindromic Lychrel Number!"     
    print numLychrel, i, LR,  PalLyc,Isp
       
  

print
print "The number of Lychrel Numbers below", numint, "is", numLychrel
print "The number of Palindromic Lychrel Numbers below", numint, "is", numPalLychrels