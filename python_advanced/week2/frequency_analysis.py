
counts = dict()
while True:
    ln = input()
    if len(ln.split()) == 0:
        break

    ws = ln.split()
    for w in ws:
        if w not in counts:
            counts[w] = 0

        counts[w] += 1

counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
for v, _ in counts:
    print(v)
