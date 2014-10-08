from itertools import combinations

x=[993, 992, 989, 983, 976, 973, 972, 969, 966, 965, 962, 960, 959, 957, 943, 941, 925, 919, 915, 914, 913, 912, 905, 901, 883, 878, 875, 873, 870, 863, 853]

sums=[]

y = combinations(x,15)

for z in y:

  zz= sum(z)
  if zz not in sums and zz>14029:
    sums.append(zz)
    print zz
