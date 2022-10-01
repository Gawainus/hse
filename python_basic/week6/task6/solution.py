
n, m = list(map(int, input().split()))

def rotate(n, m):
    arr = [input().split() for _ in range(n)]
    arr = arr[::-1]
    t = list(zip(*arr))
    for i in range(m):
        print(*t[i])


rotate(n, m)