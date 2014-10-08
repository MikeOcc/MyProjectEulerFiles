MAXD = 16
 
sumOfLength = [0] + [i * 9 * 10 ** (i-1) for i in range(1, MAXD)]
 
startOffset = [0] * (MAXD)
for i in range(2, MAXD):
    startOffset[i] = startOffset[i-1] + sumOfLength[i-1]
 
MAXS = 3 ** 11
 
def nthKDigit(num):
    # 0 based  eg 10 -> 0, 11 -> 1, 1000 -> 0, 1123 -> 123
    last = 0
    act = 9
    while num - act > 0:
        last = act
        act = 10*act + 9
    return num - last - 1
 
def getOffset(num, digits):
    return startOffset[digits] + digits * nthKDigit(num) + 1
 
def f(num):
    snum = str(num)
    occurences = []
 
    # Calculations for full number ...
    numDigits = len(snum)
    digits = numDigits
    occurences = [getOffset(num, digits)]
    while len(occurences) < num:
        digits += 1
        freeDigits = digits - numDigits
 
        # numbers xxNUM, eg 1NUM, 2NUM, 3NUM, .., 9NUM.
        shift = 10 ** numDigits
        occurences += [getOffset(i * shift + num, digits) + freeDigits
                       for i in xrange(10 ** (freeDigits-1), 10 ** freeDigits)]
 
        # numbers NUMxx
        mult = 10 ** freeDigits
        occurences += [getOffset(mult * num + i, digits) for i in xrange(0, 10 ** freeDigits)]
 
        # numbers xx NUM yy
        for prefDigits in range(1, freeDigits):
            suffDigits = freeDigits - prefDigits
 
            prefShift = 10 ** (numDigits + suffDigits)
            numShift = 10 ** suffDigits
            occurences += [getOffset(i * prefShift + num * numShift + j, digits) + prefDigits
                           for i in xrange(10 ** (prefDigits-1), 10 ** prefDigits)
                           for j in xrange(0, 10 ** suffDigits)]
 
    # Calculations for divided number on 2 parts ...
    for k in range(1, len(snum)):
        # not working in case snum = 9..., eg. 920
        sn1, sn2 = snum[:k], snum[k:]
 
        if sn2[0] == '0': continue  # We should skip leading zeros
 
        sn1p = str(int(sn1) + 1)
 
        numDigits = len(sn1) + len(sn2)
        digits = numDigits
 
        occurences += [getOffset(int(sn2 + sn1), digits) + digits - len(sn1)]
 
        for i in range(1, min(len(sn1p), len(sn2))+1):
            #nxt = str(int(sn2[i:] + sn1) + 1)
            #if snum in sn2[i:] + sn1 + nxt:
            #    occurences += [getOffset(int(sn2[i:] + sn1), digits - i) + digits - i - len(sn1)]
            if sn1p[:i] == sn2[-i:]:
                occurences += [getOffset(int(sn2[i:] + sn1), digits - i) + digits - i - len(sn1)]
 
 
        length = 0
 
        while True:
            digits += 1
            freeDigits = digits - numDigits
 
            mult = 10 ** len(sn1)
            firstPart = int(sn2) * mult * 10 ** freeDigits
            lastPart = int(sn1)
 
            # numbers N2 xx N1
            hi = 10 ** freeDigits
            if sn1 in ('9', '99', '999', '9999', '99999', '999999'):
                hi -= 1 # we cannot change sn2
                firstPartPrec = firstPart - mult * 10 ** freeDigits
                occurences.append(getOffset(firstPartPrec + (hi)*mult + lastPart, digits) + digits - len(sn1))
                length += 1
            for i in xrange(0, hi):
                occurences.append(getOffset(firstPart + i*mult + lastPart, digits) + digits - len(sn1))
                length += 1
                if length > num: break
            else:
                continue
            break
 
    unique = list(set(occurences))
    unique.sort()
 
##    if num < 1000:
##        print unique[:num]
##    else:
##        print unique[:100]
 
    return unique[num-1]
 
 
 
print "TEST"      
print 1, f(1)
print 5, f(5)
print 12, f(12)
print 7780, f(7780)
 
result = 0
for k in range(1,14):
    print k, 3 ** k,
    res = f(3 ** k)
    print res
    result += res
 
print result