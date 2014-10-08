#
#
#  Euler Problem 98
#
#
from string import strip

def retHash(s):
  return "".join(sorted(s))

f = open('words98.txt')

wl = []
wlh = [] 
sqs = []


for i in xrange(99999):
  if len(str(i*i))>7:
    sqs.append(i*i)

#print sqs

a=str(f.readlines()).strip('[]').split(",")

for c in a:
  tmp = c.strip('"').strip("'").strip('"')
  #print tmp
  if len(tmp)>1:
    wl.append(tmp)
    wlh.append(retHash(tmp))


wset = set(wlh)

for h in wset:
  if wlh.count(h)>1:
    print "#######"
    w=[]
    for i in xrange(len(wl)):
      if wlh[i] == h:
        print wl[i] 
        w.append(i)
    zz = len(w)
    for n in sqs:
     if len(str(n)) == 9 and len(set(str(n)))==len(set(wl[w[0]])):
       z = str(n)
       z = int(z[3:4]+z[8:9]+z[5:8]+z[2:3]+z[0:1]+z[4:5]+z[1:2])       #int(z[1:4]+z[0:1]+ z[4:])
       x = wl[w[0]]
       print n,x,x[3:4]+x[8:9]+x[5:8]+x[2:3]+x[0:1]+x[4:5]+x[1:2] ,z

       if z**.5 == int(z**.5):
         print "hit!", z

       






