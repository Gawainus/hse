
x_set = set()
y_set = set()

coords = []

attacking = False

for i in range(8):
    parts = input().split()
    x = int(parts[0])
    y = int(parts[1])

    if x in x_set or y in y_set:
        attacking = True
        break

    attacking_diag = False
    for xi, yi in coords:
        if abs((yi-y)/(xi-x)) == 1:
            attacking = True
            attacking_diag = True
            break
    if attacking_diag:
        break

    x_set.add(x)
    y_set.add(y)
    coords.append((x, y))

if attacking:
    print("Yes")
else:
    print("NO")





