#
#  Euler Problem 24
#  Find Millionth Lexicographic perm of
#  digits 0-9
#


def makenum(dignum):

  retnum = ""
  for i in range(0,10):
    retnum += str(dignum[i])
  return int(retnum)

basedig = [0,1,2,3,4,5,6,7,8,9]
curdig = [0,1,2,3,4,5,6,7,8,9]

len9 = 2

temp = curdig[8]
curdig[8]=curdig[9]
curdig[9]=temp

print temp
print basedig
print curdig

print makenum(curdig)

#for i in range(1,2):
  
#print basedig
  #tempdig = 
  #newdig = 