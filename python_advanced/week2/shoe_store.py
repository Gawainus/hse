size = int(input())
shoes = sorted([int(i) for i in input().split()])

count = 0
max_count = 0
for i in range(len(shoes)):
    if shoes[i] < size:
        continue

    prev = shoes[i]
    count = 1
    for j in range(i+1, len(shoes)):
        if shoes[j] >= prev + 3:
            count += 1
            prev = shoes[j]

    if count > max_count:
        max_count = count

print(max_count)
