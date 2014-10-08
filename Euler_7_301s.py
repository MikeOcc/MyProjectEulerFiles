def get_losers(n):
    count = 0
    b = 2
    c = 3
    for a in xrange(1, n + 1):
        count += (a ^ b ^ c) == 0
        b += 2
        c += 3
    return count
 
print get_losers(2 ** 30)



'''
win = [0,1]
lose = [1,1]
print "w",0,1
for i in range(2,30):

    w = 2**(i-1)
    w1 = w+win[i-2]+win[-1]
    win.append(w1)
    l = 2**len(win)
    lose.append(l-win[-1])
    print "w",w,w1,win[-1],len(win),l,l-win[-1]
 
print lose[-1]
print
print win
print lose
'''