
N = input()
N = int(N)

s = ""

for i in range(0, N):
    power_two = 2 ** i
    if power_two <= N:
        s += f"{power_two} "
    else:
        break

if s != "":
    print(s)
