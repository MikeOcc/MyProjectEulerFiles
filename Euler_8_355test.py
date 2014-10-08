from Functions import RofPrimes, RetFact,IsPrime,gcd

x = RofPrimes(2,200000)
x.append(1)
r = list(x)
x = sorted(x, reverse = True)
xs = RofPrimes(2,444)
xs = sorted(xs,reverse=False)

x.remove(421)
x.remove(443)
x.remove(349)
x.remove(379)
x.remove(241)
x.remove(83)

x.append(421)
x.append(443)
x.append(349)
x.append(379)
x.append(241)
x.append(83)

'''
x.remove(3)
xs.remove(3)
x.append(177147)
'''

#x = sorted(x, reverse = False)

ps=[]
ps2=[]

l=[]
rj=[]
exc=range(2,20)
for sp in xs:
  if sp in rj:continue
  max = 0
  supermax = 0
  superm = 0
  maxp=0
  MX = 200000
  for p in xrange(1,18):
    #if sp <6 and p<3:continue
    b = sp**p    # powers of first prime
    for m in x:
      #if sp<20 and m<150:continue
      if m in rj:continue
      v = b * m
      
      if v>MX:
        continue
        
      if v>max:

        #if sp==83:
        # print sp,p,b,m,max,max-m
        # print rj
        if v-m>supermax:    
          max=v
          supermax=max-m-sp
          superm = m
          maxp=p
          break

  ps.append(sp);ps.append(superm)
  ps2.append((sp,superm,max))
  print "max",max,sp, maxp, superm
  l.append((max,sp,superm))
  rj.append(superm);rj.append(sp)


for a,b in enumerate(ps2):
   print a, b

ps= sorted(ps)

psset = list(set(ps))
print
for z in psset:
  if ps.count(z)>1:print z,ps.count(z)

l = sorted(l,reverse = True)
print

print l
print
print sum(r)


for v in l:
  val = v[0]
  p1 = v[1]
  p2 = v[2]
  #r.append(val)

  if p1 in r and p2 in r:
    print "!!",p1,p2,":",val
    r.append(val)
    r.remove(p1)
    #if p2 in r:
    #  r.remove(p2)
  else:
   print "reject",v,p1,p2
   rj.append(v)

#r.append(1)
print
#for v in rj:
#  print v
print
print "!",sum(r)
