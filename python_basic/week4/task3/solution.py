l = input()
k = int(input())

l = l.split(' ')
l[k:] = l[k+1:]

s = ""
for i in l:
    s += f"{i} "

print(s)

