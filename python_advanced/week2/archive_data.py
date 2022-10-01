
S, N = [int(i) for i in input().split()]

us = list()
for i in range(N):
    u = int(input())
    us.append(u)

us.sort()

count = 0
for u in us:
    S -= u
    if S < 0:
        break

    count += 1

print(count)
