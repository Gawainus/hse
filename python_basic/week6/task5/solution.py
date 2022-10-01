
n, m = list(map(int, input().split()))


def transpose(n, m):
    arr = [input().split() for i in range(int(n))]
    t = list(zip(*arr))
    for i in range(m):
        print(*t[i])


transpose(n, m)


