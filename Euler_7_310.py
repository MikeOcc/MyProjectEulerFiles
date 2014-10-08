#
#
# 310
#

def MEX(s):
  i = 0
  while i in s:
    i += 1
  return i



S=set([0,1, 2,3,4,5,6,7])

print MEX(S)

exit()

ctr=0
for c in xrange(0,30):
   for b in xrange(0,30):
      for a in xrange(0,30):
        if a<=b<=c:
          a1 = (int(a**.5)**2);a2 = a-a1
          b1 = (int(b**.5)**2);b2 = b-b1
          c1 = (int(c**.5)**2);c2 = c-c1
          if a2==9:a2=0
          if b2==9:b2=0
          if c2==9:c2=0

          if a2==4:a2=0
          if b2==4:b2=0
          if c2==4:c2=0

          if a2==8:a2=0
          if b2==8:b2=0
          if c2==8:c2=0

          if a2==7:a2=3
          if b2==7:b2=3
          if c2==7:c2=3

          #if a2==6:a2=2
          #if b2==6:b2=2
          #if c2==6:c2=2

          #if a2==5:a2=1
          #if b2==5:b2=1
          #if c2==5:c2=1

          print a,b,c,":",a2,b2,c2
          if a2^b2^c2 ==0: 
            ctr+=1
            print "!",a2,b2,c2




print ctr