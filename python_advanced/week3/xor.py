def xor(x, y):
    return str(x ^ y)


a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

print(" ".join(map(xor, a1,  a2)))
