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
  P.append(n*(3*n-1)/2)
  if len(str(n*(2*n-1)))==4 and "0" not in str(n*(2*n-1)):
    HX.append(n*(2*n-1))
  HP.append(n*(5*n-3)/2)
  O.append(n*(3*n-2))




  t1="".join(  list(sorted(str( n*(n+1)/2 ) )) )
  s1="".join(  list(sorted(str(  n*n ))) )
  p1="".join(  list(sorted(str( n*(3*n-1)/2 )))) 
  hx1= "".join( list(sorted(str(n*(2*n-1))) ))
  hp1= "".join( list(sorted(str(n*(5*n-3)/2)) ))
  o1 = "".join(  list(sorted(str( n*(3*n-2) )))  )

  Th.append(t1)
  Sh.append(s1)
  Ph.append(p1)
  HXh.append(hx1)
  HPh.append(hp1)
  Oh.append(o1)
  '''
  print n," )############"
  print T[ctr],t1
  print S[ctr],s1
  print P[ctr],p1
  print HX[ctr],hx1
  print HP[ctr],hp1
  print O[ctr],o1
  '''

print T

print 

print HX

exit()


print "#############################"
print Th
print 
print Sh
print 
print Ph
print 
print HXh
print 
print HPh
print 
print Oh
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
print Th
print 
print Sh
print 
print Ph
print 
print HXh
print 
print HPh
print 
print Oh
print 

print "%%%%%%%%%%%%%%%"


print Oh
print "====="
print set(Oh)
print
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
