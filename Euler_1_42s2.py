import math
print sum([int((math.sqrt(1+8.0*sum([ord(c) - 63 for c in word.rstrip()]))-1)/2) for word in file('words.txt')]) 