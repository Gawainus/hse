N = int(input())

ws = []
for _ in range(N):
    w = input()
    ws.append(w)

ws = sorted(ws, key=lambda x: (len(x), x[::-1]))

for w in ws:
    print(w)
