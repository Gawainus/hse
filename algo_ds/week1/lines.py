
def lines(a):
    # print(a)
    if not a:
        return 0

    start = 0
    prev = a[start]
    for i in range(1, len(a)):
        if a[i] == prev:
            continue

        if (i - 1) - start > 1:
            # print(start, i)
            return (i - start) + lines(a[0:start] + a[i:])

        start = i
        prev = a[i]

    if len(a) - start > 2:
        return len(a) - start

    return 0


# print(lines([2, 2, 2, 1, 1, 1]))
