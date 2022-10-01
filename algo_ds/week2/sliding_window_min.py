
from collections import deque


def sliding_window_min(a, k):
    size = len(a)
    o = []
    if size < k:
        return o

    d = deque()
    d.append(a[0])
    for i, x in enumerate(a[1:k]):
        while d and x < d[-1]:
            d.pop()

        d.append(x)

    for i, x in enumerate(a[k:]):
        o.append(d[0])

        x_out = a[i]
        # print(i, x_out, x, d)
        while d and x < d[-1]:
            d.pop()

        d.append(x)
        if x_out == d[0]:
            d.popleft()

    o.append(d[0])
    return o


if __name__ == '__main__':
    print(sliding_window_min([3, 1, 1, 5, 0, 4, 5], 3))
    print(sliding_window_min([1, 3, 4, 5, 2, 7], 3))
