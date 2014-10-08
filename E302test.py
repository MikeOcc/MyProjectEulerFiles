
bump = 0

factlist = []
numlist = []
powerlist = []
numdict ={}
ctr=0
for q in range(0,5):  #23
  if q==1:continue
  for p in range(0,5):  #19
    if p==1:continue
    for o in range(0,7):  #17
      if o==1:continue
      for n in range(0,7+bump):  #13
        if n==1:continue
        for m in range(0,7+bump):  #11
          if m==1:continue
          for l in range (0,8+bump):  #7
            if l==1:continue
            for k in range(0,13+bump):  #5
              if k==1:continue
              for j in range(0,23+bump):  #3
                if j==1:continue
                for i in range (0,25+bump):  #2
                    if i==1:continue
                    ctr +=1        
                    fact = (2**i) * (3**j) * (5**k) * (7**l) * (11**m) * (13**n) * (17**o) * (19**p) * (23**q)
                    print ctr,")",fact
                    factlist.append(fact)
                    powerlist.append((i,j,k,l,m,n,o,p,q))
                    numdict[fact] = (i,j,k,l,m,n,o,p,q)


print "factlist:", factlist

print 
print "factlist sort:", factlist.sort()

print
print "powerless:", powerless

print
print "powerless sort:", powerlist.sort()

print  
print "numb dict:" ,numdict

print "numb dict sort:", numdict.sort()

                    

