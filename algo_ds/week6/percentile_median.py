
def median2(a, b):
    """
    median of two numerics
    :param a: numeric
    :param b: numeric
    :return: median
    """
    return min(a, b)


def median3(a, b, c):
    """
    median of three numerics
    :param a: numeric
    :param b: numeric
    :param c: numeric
    :return: median
    """
    arr = [a, b, c]
    return sorted(arr)[1]


def median4(a, b, c, d):
    """
    median of four numerics
    :param a: numeric
    :param b: numeric
    :param c: numeric
    :param d: numeric
    :return: median
    """
    arr = [a, b, c, d]
    return sorted(arr)[1]


def medianArr(arr, n):
    """
    :param arr: iterable of numerics
    :param n: length
    :return: median
    """
    if n == 0:
        return -1
    if n % 2 == 0:
        return (arr[n / 2 - 1] + arr[n / 2]) / 2
    return arr[n / 2]


def find_percentile_base(a, len_a, b, len_b, p):
    """
    This function assumes that N is smaller than or equal to M
    This function returns -1 if both arrays are empty
    :param a:
    :param len_a:
    :param b:
    :param len_b:
    :param p: percentitle
    :return:
    """
    # print("find_percentile_base")
    # print(len_a, a)
    # print(len_b, b)

    print("array a:", len_a, a)
    print("array b:", len_b, b)
    # print("mid_a:", mid_a, "value:", a[mid_a])
    # print("mid_b:", mid_b, "value:", b[mid_b])
    # print("idx", idx)
    print()
    if len_a == 0:
        return medianArr(b, len_b)

    if len_a == 1:
        if len_b == 1:
            return median2(a[0], b[0])

        if len_b % 2 == 1:
            # Case 2: If the larger array has odd number of elements,
            # then consider the middle 3 elements of larger array and
            # the only element of smaller array. Take few examples
            # like following
            # A = {9}, B[] = {5, 8, 10, 20, 30} and
            # A[] = {1}, B[] = {5, 8, 10, 20, 30}
            return median2(b[len_b // 2], median3(a[0], b[len_b // 2 - 1], b[len_b // 2 + 1]))
        else:
            # Case 3: If the larger array has even number of element,
            # then median will be one of the following 3 elements
            # ... The middle two elements of larger array
            # ... The only element of smaller array
            return median3(b[len_b // 2], b[len_b // 2 - 1], a[0])

    # If the smaller array has two elements
    elif len_a == 2:
        if len_b == 2:
            # Case 4: If the larger array also has two elements,
            # simply call median4()
            return median4(a[0], a[1], b[0], b[1])

        if len_b % 2 == 1:
            # Case 5: If the larger array has odd number of elements,
            # then median will be one of the following 3 elements
            # 1. Middle element of larger array
            # 2. Max of first element of smaller array and element
            # just before the middle in bigger array
            # 3. Min of second element of smaller array and element
            # just after the middle in bigger array
            return median3(
                b[len_b // 2],
                max(a[0], b[len_b // 2 - 1]),
                min(a[1], b[len_b // 2 + 1]))
        else:
            # Case 6: If the larger array has even number of elements,
            # then median will be one of the following 4 elements
            # 1) & 2) The middle two elements of larger array
            # 3) Max of first element of smaller array and element
            # just before the first middle element in bigger array
            # 4. Min of second element of smaller array and element
            # just after the second middle in bigger array
            return median4(
                b[len_b // 2],
                b[len_b // 2 - 1],
                max(a[0], b[len_b // 2 - 2]),
                min(a[1], b[len_b // 2 + 1]))

    idx_a = (len_a - 1) // 2
    idx_b = (len_b - 1) // 2

    if a[idx_a] <= b[idx_b]:
        return find_percentile_base(a[idx_a:], len_a - idx_a, b[:idx_b + 1], idx_b, p)
    else:
        return find_percentile_base(a[:idx_a + 1], idx_a, b[idx_a:], len_b - idx_a, p)


def find_percentile(a, b, p):
    import math
    if not a and not b:
        return -1

    len_a = len(a)
    len_b = len(b)
    idx = math.ceil(p * (len_a + len_b) / 100) - 1
    print("Index", idx, "Answer:", sorted(a + b)[idx])
    print("array a:", len_a, a)
    print("array b:", len_b, b)
    print()

    if len_a > len_b:
        return find_percentile_base(b, len_b, a, len_a, p)
    return find_percentile_base(a, len_a, b, len_b, p)


# some test code
if __name__ == "__main__":
    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # should print 7
    # print(find_percentile(test_a, test_b, test_p))

    # test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # should print 6
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # # should print 20
    # print(find_percentile(test_a, test_b, test_p))
    #
    # test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # # should print 20
    # print(find_percentile(test_a, test_b, test_p))

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
    p = 50

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
    print(find_percentile(a, b, p))
