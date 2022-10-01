import math
# import numpy as np


def weighted_edistance(A, B, wdel, wins, wsub):
    n = len(A)
    m = len(B)

    # d = np.array([[0] * (m + 1) for _ in range(n + 1)])
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1):
        d[0][j] = j * wins

    for i in range(1, n + 1):
        d[i][0] = i * wdel
    # print(d)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # print(A[:i], B[:j])
            if A[i - 1] == B[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(
                    wdel + d[i - 1][j],
                    wins + d[i][j - 1],
                    wsub + d[i - 1][j - 1])

            # print(d)

    return d[n][m]


def edistance(A, B):
    return weighted_edistance(A, B, 1, 1, 1)


def edistance_substring(A, B):
    n = len(A)
    m = len(B)

    d = [[0] * (m + 1) for _ in range(n + 1)]
    # d = np.array([[0] * (m + 1) for _ in range(n + 1)])
    for j in range(1, m + 1):
        d[0][j] = j

    # print(d)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c_delete = 1 if j < m else 0
            c_tail = c_delete + d[i - 1][j]
            # print(A[:i], B[:j])
            if A[i - 1] == B[j - 1]:
                d[i][j] = min(d[i - 1][j - 1], c_tail)
            else:
                d[i][j] = min(
                    c_tail,
                    1 + d[i][j - 1],
                    1 + d[i - 1][j - 1])

            # print(d)

    return d[n][m]


if __name__ == "__main__":
    # should print 3
    # print(edistance("good", "bad"))
    # should print 7
    # print(weighted_edistance("good", "bad", 1, 2, 5))
    print(edistance_substring("badgood", "bad"))
