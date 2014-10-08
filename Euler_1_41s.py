def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]
 
 
def isPrime(x):
    prime = True
    if x < 2:
        prime = False
    else:
        for f in range(2, int(x ** 0.5)):
            if not x % f:
                prime = False
                break
 
    return prime
 
 
panprimes = []
legalSizes = [7,4]
for length in [7,4]:
    pandigital = ''
 
    for x in range(1, length + 1):
        pandigital += str(x)
 
    for perm in all_perms(pandigital):
        if isPrime(int(perm)):
            panprimes.append(int(perm))
 
    if len(panprimes):
        panprimes.sort()
        print panprimes[len(panprimes) - 1]
        quit()