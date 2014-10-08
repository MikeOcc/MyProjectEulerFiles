s = [{1:1, 4:1}, {5:1}]

for i in range(3,101):

    i2 = i*i
    if i<52:
        t = [s[0].copy()]
        t[0][i2] = 1
    else: t = []

    for j in range(1, len(s)):
        t.append(s[j].copy())
        for k in s[j-1]:
            if i2+k in t[-1]: t[-1][i2+k] += s[j-1][k]
            else: t[-1][i2+k] = s[j-1][k]

    if i<51: t.append({(i2+i)*(2*i+1)//6: 1})

    del s

    s = t

print(sum([i for i in s[0] if s[0][i] == 1]))

for i in s:
  print i