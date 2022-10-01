n = input()

def pd(n):
    if len(n) == 0:
        return 0

    return int(n[0]) + pd(n[1:])


print(pd(n))
