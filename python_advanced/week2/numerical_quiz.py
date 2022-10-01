def cmp(x):
    size = len(x)
    v = 0
    for i in range(int(size/2)):
        v += int(x[i]) - int(x[size - i - 1])

    return v, int(x)


N = int(input())

ws = []
for _ in range(N):
    w = input()
    ws.append(w)


ws = sorted(ws, key=cmp)

for w in ws:
    print(w)
