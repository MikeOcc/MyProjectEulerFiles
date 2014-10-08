#
#



from Functions3 import GCD,gcd
from itertools import product
from Functions import RofPrimes,RetFact

def notcoprime(cp,Y):
  for yy in Y:
    if gcd(yy,cp)!=1:
      return yy
  return -1

#####################

MX=200000
x = RofPrimes(2,MX)
x2 = RofPrimes(2,444) 
#x.append(1)

T=[]

for i in xrange(len(x2)):
  tmp=[]
  p=0
  while 1:
    p+=1
    v0=x[i]
    v = x[i]**p
    if v>MX or v0>=MX:break
    #print "!",i,p,x[i],v
    tmp.append(v)

  tmp2=list(tmp)
  #print "t",tmp2
  for z in tmp2:
   for zz in x:
     #if z==443:print "Z",z,zz
     if z*zz <=MX and zz>=v0 and z*zz not in tmp:
       #print "!!!!",z,v0
       tmp.append(z*zz)
  
  #tmp=sorted(tmp,reverse=True)
  if len(tmp)>1:
    if 443 in tmp:tmp.remove(443)
    if 439 in tmp:tmp.remove(439)
    tmp=sorted(tmp,reverse=False)[-4:]
    #print tmp
    T.append(tmp) 
print
print
#exit()
print
W=[]
for a,b in enumerate(T):
#   print a,b
   W.append(b[-4:])
T=[]
print
print

#print W
#L= list(product(*W))

max = 0
x.append(1)
Sum = sum(x)
maxlist=[]

#print tmp
#tmp=list(x)
for l in product(*W):
  #l=sorted(l,reverse = False)
  tmp=list(x)
  #if GCD(l)>1:continue
  #s = sum(l)
  #print l, s
  tsum = 0
  for j in l:
    #print j
    if j in tmp:continue
    f = sorted(list(set(RetFact(j))))
    #print "F",f
    if len(f)==1:
      old = notcoprime(f[0],tmp)
      #print "Old",old
      if j > old:
        tsum+=j-old;tmp.append(j);tmp.remove(old)
      continue
      
    #print "j",j,f
    f1 = f[0];f2 = f[1]

    if j/f1!=f2:
      f1 = j/f2
    elif j/f2!=f1:
      f2 = j/f1
    old1,old2=0,0
    old1 = notcoprime(f1,tmp)
    old2 = notcoprime(f2,tmp)
    if old1> 0 and old2 > 0:
      if j> old1 + old2:
        tsum+=j-old1-old2;tmp.append(j)
        #print j, old1, old2
        tmp.remove(old1)
        tmp.remove(old2)
    elif old1>0:
      if j> old1:
        tsum+=j-old1;tmp.append(j);tmp.remove(old1)

    elif old2>0:
      if j> old2:
        tsum+=j-old2;tmp.append(j);tmp.remove(old2)
    else:
      tsum+=j;tmp.append(j)
  if Sum + tsum>max:
    max=Sum+tsum
    print "new sum", max
    maxlist = tmp
  


print
print 
print "Max =",max
print "Max Set =",maxlist














