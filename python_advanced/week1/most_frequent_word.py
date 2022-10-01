
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

most = 0
for v in counts.values():
    if v > most:
        most = v

candidates = []
for k, v in counts.items():
    if v == most:
        candidates.append(k)

print(sorted(candidates)[0])
