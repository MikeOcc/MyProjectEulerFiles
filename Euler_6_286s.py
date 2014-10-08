#@memoize
def f(h,t,q):
    if h>t or h<0: return 0
    if t==0: return 1
    return (1-float(t)/q)*f(h-1,t-1,q) + (float(t)/q)*f(h,t-1,q)
    
lo,hi,goal=50,100,.02
for binaryTrials in range(0,40):
    q=(lo+hi)/2.0
    if f(20,50,q)<goal:hi=q
    else:lo=q
    
print round(q,10)

#52.6494571953