a = int(input())
b = int(input())

s = ""

if a < b:
    for i in range(a, b + 1):
        s += f"{i} "
else:
    for i in range(b, a+1):
        s = f"{i} " + s

print(s)




