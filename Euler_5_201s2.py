def p201():
    global count, k
    k = 100
    squares = [x*x for x in xrange(1, k+1)]
    max_sum = sum(squares[:k//2])*1.06
 
    count = 0
    sums = {}
    def explore(start, current_sum=0, level=0):
        global count, k
        if level == k//2:
            sums[current_sum] = sums.get(current_sum, 0) + 1
            count += 1
            return
        for m in xrange(start, k + 1):
            if current_sum + m*m > max_sum:
                return
            prev_count = count
            explore(m + 1, current_sum + m*m, level+1)
            if prev_count == count:
                break
 
    explore(1)
    print sum(squares)*sum(1 for x in sums if sums[x] == 1)
 
p201()