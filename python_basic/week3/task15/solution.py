a = int(input())
b = int(input())

for i in range(a, b+1):
    i = str(i)
    i_r = i[::-1]
    if i == i_r:
        print(i)