
N = input()
N = int(N)

s = ""

for i in range(N):
    base = i + 1
    sq = base ** 2
    if sq <= N:
        s += f"{sq} "
    else:
        break

if s != "":
    print(s)

