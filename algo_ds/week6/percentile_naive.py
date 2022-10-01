import sys
sys.setrecursionlimit(99)


def get_mid_idx(length):
    """
    Calculate the index of the middle
    :param length:
    :return: the index
    """
    if length % 2 == 0:
        return length // 2 - 1
    else:
        return length // 2


def brute_count(a, len_a, b, len_b, idx):
    print("brute_count")
    print("array a:", len(a), a)
    print("array b:", len(b), b)
    print("idx", idx)

    a_limit = min(len_a, idx+1)
    b_limit = min(len_b, idx+1)
    a_head = a[:a_limit]
    b_head = b[:b_limit]
    a_head.extend(b_head)
    merged = sorted(a_head)
    print("merged", merged)
    return merged[idx]


def find_percentile_base(a, len_a, b, len_b, idx):
    """
    :param a:
    :param len_a:
    :param b:
    :param len_b:
    :param idx:
    :return:
    """
    if len_a <= 2 or len_b <= 2:
        return brute_count(a, len_a, b, len_b, idx)

    if idx < 4:
        return brute_count(a, len_a, b, len_b, idx)

    mid_a = get_mid_idx(len_a)
    mid_b = get_mid_idx(len_b)
    print("find_percentile_base")
    print("array a:", len_a, a)
    print("array b:", len_b, b)
    print("mid_a:", mid_a, "value:", a[mid_a])
    print("mid_b:", mid_b, "value:", b[mid_b])
    print("idx", idx)
    print()

    if a[mid_a] < b[mid_b]:
        len_a = len_a - mid_a
        idx_new = idx - mid_a
        if len_a + len_b < idx_new or idx_new < 0:# or idx_new < mid_a:
            return brute_count(a, len_a, b, len_b, idx)

        a = a[mid_a:]
        return find_percentile_base(a, len_a, b, len_b, idx_new)
    else:
        len_b = len_b - mid_b
        idx_new = idx - mid_b
        if len_a + len_b < idx_new or idx_new < 0:# or idx_new < mid_b:
            return brute_count(a, len_a, b, len_b, idx)

        b = b[mid_b:]
        return find_percentile_base(a, len_a, b, len_b, idx_new)


def find_percentile(a, b, p):
    import math
    if not a and not b:
        return -1

    len_a = len(a)
    len_b = len(b)
    idx = math.ceil(p * (len_a + len_b) / 100) - 1
    print(sorted(a + b))
    print("Index", idx, "Answer:", sorted(a + b)[idx])
    print("array a:", len_a, a)
    print("array b:", len_b, b)
    # print()

    if len_a == 0:
        return b[idx]
    if len_b == 0:
        return a[idx]

    on_a = a[0] < b[0]
    if on_a:
        i = 1
        j = 0
    else:
        i = 0
        j = 1
    print(0, i, a[i], j, b[j], on_a, "i+j=", i + j)
    for k in range(1, idx):
        if i == len_a - 1:
            j += 1
            on_a = False
            print(k, i, a[i], j, b[j], on_a, "i+j=", i+j)
            continue
        if j == len_b - 1:
            i += 1
            on_a = True
            print(k, i, a[i], j, b[j], on_a, "i+j=", i+j)
            continue

        if a[i] < b[j]:
            i += 1
            on_a = True
        else:
            j += 1
            on_a = False

        print(k, i, a[i], j, b[j], on_a, "i+j=", i+j)

    ret = a[i] if on_a else b[j]
    return ret


    #
    # if len_a < len_b:
    #     return find_percentile_base(a, len_a, b, len_b, idx)
    # else:
    #     return find_percentile_base(b, len_b, a, len_a, idx)


if __name__ == "__main__":
    # test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # # should print 7
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # # should print 6
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [1, 2, 7, 8], [2, 6, 12], 50
    # # should print 6
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [2, 7, 8], [2, 6, 12], 50
    # # should print 6
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # # should print 20
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # # should print 20
    # print(find_percentile(test_a, test_b, test_p))

    import math
    from numpy.random import seed
    from numpy.random import randint
    # seed(7)
    # a = sorted(randint(100, size=10))
    # b = sorted(randint(100, size=100))
    # p = 50
    # print(find_percentile(a, b, p))
    #
    # seed(7)
    # a = sorted(randint(100, size=7))
    # b = sorted(randint(100, size=100))
    # p = 50
    # print(find_percentile(a, b, p))

    # seed(13)
    # a = sorted(randint(100, size=7))
    # b = sorted(randint(100, size=100))
    # p = 50
    # print(find_percentile(a, b, p))

    seed(13)
    a = sorted(randint(100, size=27))
    b = sorted(randint(100, size=3))
    p = 50
    print(find_percentile(a, b, p))
