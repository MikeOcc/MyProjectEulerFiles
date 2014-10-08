#
#
#  Euler 168
#
#


s=0
for l in range(1,100): 
    for m in range(1,10):
        z=m*((10**(l+1))-1) 
        print "z",l,m,z       
        for k in range(1,10):
            x = z / (10 * k - 1)            
            if(x*(10*k-1)==z):
                if(x>=10**l):
                    print int(x)
                    s=s+int(x)                  
print s%100000