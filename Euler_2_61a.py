#
# Euler Problem 61
#
# []

T,S,P,HX,HP,O=[],[],[],[],[],[]
Th,Sh,Ph,HXh,HPh,Oh=[],[],[],[],[],[]

ctr = -1
for n in range(0,142):
  ctr+=1
  if len(str(n*(n+1)/2))==4 and "0" not in str(n*(n+1)/2):
    T.append(n*(n+1)/2)
  if len(str(n*n))==4 and "0" not in str(n*n):
    S.append(n*n)
  if len(str(n*(3*n-1)/2))==4 and "0" not in str(n*(3*n-1)/2):
    P.append(n*(3*n-1)/2)
  if len(str(n*(2*n-1)))==4 and "0" not in str(n*(2*n-1)):
    HX.append(n*(2*n-1))
  if len(str(n*(5*n-3)/2))==4 and "0" not in str(n*(5*n-3)/2):
    HP.append(n*(5*n-3)/2)
  if len(str(n*(3*n-2)))==4 and "0" not in str(n*(3*n-2)):
    O.append(n*(3*n-2))



print "#############################"

print O
print
print HP
print
print
for v in T:
  for w in P:
    for x in O:
      for y in HP:
        for z in HX:
         for s in S:
            if (str(y)[2:]==str(x)[:2] and str(x)[2:]==str(z)[:2] and str(z)[2:]==str(w)[:2] and str(w)[2:]==str(v)[:2] \
            and str(v)[2:]==str(s)[:2] ):
              print "4" ,y,x,z,w,v,s

print "Total is", y+x+z+w+v+s

   #else:
   #  O.remove(x);HP.remove(y)

exit()

print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

print "%%%%%%%%%%%%%%%"

print "%%%%%%%%%%%%%%%"




#U = set(Oh).intersection(set(HPh));print U
#U = U.intersection(set(HXh));print U
U = set(HXh).intersection(set(HPh));print U
U = U.intersection(set(Ph));print U
U = U.intersection(set(Sh));print U
U = U.intersection(set(Th));print U
#print U

hashm = '1128'
summ = 0
for i in xrange(len(Oh)):
  if Oh[i] == hashm:
   print "O:",O[i]
   summ+= O[i]

for i in xrange(len(HPh)):
  if HPh[i] == hashm:
   print "HP:",HP[i]
   summ+= HP[i]

for i in xrange(len(HXh)):
  if HXh[i] == hashm:
   print "HX:",HX[i]
   summ+= HX[i]

for i in xrange(len(Ph)):
  if Ph[i] == hashm:
   print "P:",P[i]
   summ+= P[i]

for i in xrange(len(Sh)):
  if Sh[i] == hashm:
   print "S:",S[i]
   summ+= S[i]
   break

for i in xrange(len(Th)):
  if Th[i] == hashm:
   print "T:",T[i]
   summ+= T[i]

print "The sum of the cyclic numbers is",summ



print T
print 
print S
print 
print P
print 
print HX
print 
print HP
print 
print O
