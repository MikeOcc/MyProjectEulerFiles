#
#
#
#
#
from Functions import RetFact


d = 12000.

f = RetFact(d)

ctr=0
for i in xrange(4001,6000):
   #if  not (d%i == 0): ctr+=1
   a = RetFact(i)
   if bool(set(a) & set(f))==False:
     print i,":",a
     ctr+=1
print ctr

u= int(1999./3.)
v= int(1999./2.)
w= int(1999./5.)
x= int(1999./6.)
y= int(1999./10.)
z= int(1999./15.)
z1= int(1999./30.)

tot = u+v+w-x-y-z  #-z1

print tot, 1999-tot