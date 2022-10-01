N, num_rows = [int(i) for i in input().split()]

s_days = set()
for i in range(num_rows):
    s, c = [int(i) for i in input().split()]
    for j in range(N):
        d = s + c * j
        if d > N:
            break

        s_days.add(d)

for j in range(N):
    sat = 6 + 7 * j
    sun = 7 + 7 * j
    if sat > N:
        break

    s_days.discard(sat)
    s_days.discard(sun)

print(len(s_days))
