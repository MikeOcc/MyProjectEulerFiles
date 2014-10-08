p=set(primes)
def trunc(x):
    global p
    if x not in p: return False
    sx = `x`
    for i in range(1, len(sx)):
        if int(sx[i:]) not in p: return False
        if int(sx[:i]) not in p: return False
    return True
 
[x for x in primes if trunc(x) and x > 7]