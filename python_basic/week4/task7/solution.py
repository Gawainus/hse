l = input()
h = int(input())

if len(l) == 0:
    print(1)
    exit(0)

l = [int(i) for i in l.split()]

for i, _h in enumerate(l):
    if h > _h:
        break

print(i+1)

