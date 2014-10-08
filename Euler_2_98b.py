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


for i in xrange(2,999999):
  if len(str(i*i))>2:
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
maxsqr = 0
maxword = ""
for h in wset:
  if wlh.count(h)>1:
    print "#######"
    w=[]
    for i in xrange(len(wl)):
      if wlh[i] == h:
        print wl[i] 
        w.append(i)

    print "_______________"
    wrd1 = wl[w[0]]              
    wrd2 = wl[w[1]]
    zz = len(str(wl[w[0]]))
    for n in sqs:
      if len(str(n)) == zz and len(set(str(n)))==len(set(wl[w[0]])):

        m=[]
        num=[]
        key1=[]
        nstr = str(n)
        for v in xrange(zz):
          m.append(nstr[v])
          key1.append(wrd1[v])
        
        for u in list(wrd2):
          for k in xrange(zz):
            if key1[k]==u:
              num.append(m[k])

        m = int("".join(m)); num = int("".join(num))
        #print wrd1,m," ",wrd2,num
 
        zzz = num**.5
        if zzz == int(zzz) and len(str(zzz))==len(str(m)):
           print "hit!", wrd1, wrd2, n, num
           if num > maxsqr:
              maxsqr=num
              maxwrd=wrd2
        #else:
        #   print "miss.",wrd1,wrd2,n,num,num**.5

print "Max square is",maxsqr,"for word", maxwrd




