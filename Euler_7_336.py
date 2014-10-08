




train = "DACB"

llist = list(train)

print llist

llist =llist[0:1] + llist[:0:-1]

print llist

llist =llist[::-1]

print llist

print llist[0:2] , llist[:1:-1]
llist =llist[0:2] + llist[:1:-1]

print llist

print llist[0:1] , llist[:0:-1]
llist =llist[0:1] + llist[:0:-1]

print llist

print llist[0:2] , llist[:1:-1]
llist =llist[0:2] + llist[:1:-1]

print llist
