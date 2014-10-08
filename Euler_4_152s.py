def problem152():
    from collections import defaultdict
 
    N = 80
 
    # Make a whole-number problem.
    denominators = [i**2 for i in range(2, N+1)]
    d = lcmAll(denominators)
    addends = {d//x for x in denominators}
    target = d * 1 // 2
 
    # Reduce the set as much as possible.
    for x in range(2, 300):
        # Eliminate addends that do not participate in any sum to target
        # modulo x.  Any addends that are themselves 0 modulo x can, trivially,
        # participate in such a sum.  So here we only consider those addends
        # that are nonzero modulo x.
        #
        # The order of items in this list can be whatever, but the indices of
        # the array are used to make bitsets in the loop below.
        relevant = [a for a in addends if a % x != 0]
 
        sums = [0] * x
        sums[0] = 1<<len(relevant)
        for i, a in enumerate(relevant):
            bit = 1 << i
            for j, bitset in enumerate(sums[:]):
                if bitset:
                    sums[(j + a) % x] |= bitset | bit
 
        participant_bitset = sums[target % x]
        participants = {a for i, a in enumerate(relevant) if participant_bitset & (1 << i)}
 
        dead = set(relevant) - participants
        #print(x, [intSqrt(d//a) for a in dead])
        addends -= dead
        #print(len(addends), "addends remaining")
 
    #print("live numbers:", [intSqrt(d//a) for a in addends])
 
    def allSums(addends):  # returns a histogram
        combos = defaultdict(int)
        combos[0] = 1
        for a in addends:
            for t, n in list(combos.items()):
                combos[t + a] += n
        return combos
 
    addends = list(addends)
    left = allSums(addends[0::2])
    right = allSums(addends[1::2])
    return sum(right[target - x] * n for x, n in left.items())


print problem152()