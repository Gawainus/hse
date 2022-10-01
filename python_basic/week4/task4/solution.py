l = input()
l2 = input()

l = l.split(' ')
l2 = l2.split(' ')

k = int(l2[0])
c = l2[1]

l.insert(k, c)

s = ""
for i in l:
    s += f"{i} "

print(s)

