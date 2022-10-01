l = input()
l = l.split(' ')
l = [int(i) for i in l]

d = dict()
for i in l:
    d[i] = 0

for i in l:
    d[i] += 1

s = ""
for i in l:
    if d[i] == 1:
        s += f"{i} "

print(s)
