s = input()

l = len(s)


if l % 2 == 0:
    e = int(l/2)
else:
    e = int(l/2) + 1

print(s[e:] + s[:e])
