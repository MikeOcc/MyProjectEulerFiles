#
#  Euler Problem 104
#
#

def IsPan(s):
  
  return "".join(sorted(s))=='123456789'

###########

F1 = 1
F2 = 1

for i in xrange(112749-2):
   F = F2 + F1
   F1 = F2
   F2 = F
   Fstre = str(F)[-9:]
   Fstrb = str(F)[:9]

   if IsPan(Fstrb) and IsPan(Fstre):
     print "k is", i+3
     break

   
#print i+3,F
#print Fstr, IsPan(Fstr)

  