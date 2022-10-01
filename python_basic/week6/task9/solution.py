a = int(input())
b = int(input())

def sum(a, b):
    if a == 0 and b == 0:
        return 0

    if a == 0:
        if b > 0:
            return 1 + sum(0, b - 1)
        else:
            return -1 + sum(0, b + 1)

    if b == 0:
        if 1 > 0:
            return 1 + sum(a - 1, 0)
        else:
            return -1 + sum(a + 1, 0)


    if a > 0 and b > 0:
        return 2 + sum(a-1, b-1)
    elif a > 0 and b < 0:
        return sum(a-1, b+1)
    elif a < 0 and b < 0:
        return -2 + sum(a+1, b+1)
    else:
        return sum(a+1, b-1)

print(sum(a, b))

