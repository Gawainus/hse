x = int(input())
p = int(input())
y = int(input())

s = x
r = 1 + p/100
n = 0

while True:
    if s >= y:
        print(n)
        break

    s = r * s
    s = int(s*100)/100
    n += 1


