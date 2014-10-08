from time import time
st = time()


'''
max_digits=20 # Finds all terms with <= 20 digits
maxval=10**max_digits
found =[]
for sod in range(2,9*max_digits):
    x=sod
    while x < maxval:
        if sum(int(i) for i in str(x)) == sod:
            if x>10: found.append(x)
        x*=sod
 
found.sort()
print found[29]
'''

from time import time
def sumofdigits(n):
    total = 0
    while n>0:
        total += n%10
        n //= 10
    return total
start = time()
lst = []
for e in range(2,11):
    s = 2
    p = s**e
    while p < 10**(2*e):
        if s == sumofdigits(p):
            lst.append(p)
            #print(p,e)
        s+=1
        p = s**e
lst.sort()
print (lst[29],'in',time()-start,'seconds')

print "process time is", time()-st