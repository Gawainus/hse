import numpy

def knapsack_full(W, V, C):
    n = len(W)
    tbl = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(C + 1):
            tbl[i][j] = tbl[i - 1][j]
            if j >= W[i - 1]:
                tbl[i][j] = max(
                    tbl[i][j],
                    tbl[i - 1][j - W[i - 1]] + V[i - 1]
                )

    knapsack = []
    i = n
    j = C
    while i > 0:
        if tbl[i][j] != tbl[i - 1][j]:
            j -= W[i - 1]
            knapsack.append(i - 1)
        i -= 1

    print(numpy.array(tbl))
    print(knapsack)
    return tbl[-1][-1], knapsack


if __name__ == '__main__':
    w = [3, 3, 3, 1, 1, 1, 1, 1, 1]
    v = [5, 4, 3, 5, 11, 5, 7, 11, 1]
    c = 12
    knapsack_full(w, v, c)
