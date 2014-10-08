maxn = 100000001;
 
a=[0]*maxn
 

n = 100000000

for i in xrange(1, n+1):  #  (int i = 1; i <= n; i++)
    a[i] = i;

#print a

ret = 0;


for i in xrange(1,n+1):   #(int i = 1; i <= n; i++):
    ret += (n / i - 1) * a[i];
    for j in xrange(i+1,n+1,i):  # (int j = i + i; j <= n; j += i)
       a[j] -= a[i];

print ret * 6

