from time import time

st = time()

# for i in xrange(500,25,-1):
  # if pow(i,i,250)==0:
    # print i
	
d={}
for i in xrange(1,250251):
  d[i]=pow(i,i,250)
  
# for i in xrange(1,41):
  # print i, d[i]
  
# for i in xrange(1,100):
  # for j in xrange(1,100):
    # if j>=i:continue
    # if (d[i] + d[j])%250==0:
      # print i,j,":",d[i],d[j]
	  
# for i in xrange(1,100):
  # for j in xrange(1,100):
    # for k in xrange(1,100):
      # if j>=i:continue
      # if k>=j:continue
      # if (d[i] + d[j] + d[k])%250==0:
        # print i,j,k,":",d[i],d[j],d[k]
		
f={}

for i in d:
  x=d[i]
  if x in f:
    f[x] +=1
  else:
    f[x] = 1
	
#print f

numsets = [0]*250;
numsets[0] = 1
tot = 1
for i in xrange(250):
  if i not in f: continue
  #if i==1:print numsets
  for j in xrange(f[i]):
    numsets = [(numsets[k] + numsets[(k-i)]) % 10**16 for k in range(250)]
    #if i==0:print numsets
    #print
    #for k in xrange(250):
       #z = numsets[k] + numsets[k-i]
       #tot[k]= z

print "Number of subsets is ", numsets[0] -1
print "Time elapsed is ", time()-st


