s = input()

parts = s.split(' ')
l = [int(i) for i in parts]

idx = 0
maxi = l[0]
for i, e in enumerate(l):
    if e > maxi:
        maxi = e
        idx = i

print(f'{maxi} {idx}')
