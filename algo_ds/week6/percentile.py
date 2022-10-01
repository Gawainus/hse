import math
import time

def find_percentile_base(a, b, len_a, k):
    """
    1. Solution explanation: The idea is to put a bar `k` in the merged a and b
    such that there is p/100 * K numbers to the left of `k`.
    But we do not want to merge the array. So we want to start from the middle
    of the array a and at (k- len_a)//2 of array b and move both separator to
    form index `k`. See the inline explanation for details.

    2. Time complexity:
    O(log(min(m, n)) meaning logarithm of the length of the shorter array

    3. Space complexity:
    O(1), only some vars need to be allocated with no relationship to the array
    size

    4. Correctness proof
        there are two cases:
        1. `left` moves to the right, m1 + 1
        2. `right` moves to the left, right = m1

        So the loop has to terminate

    :param a: [int]
    :param b: [int]
    :param len_a: int
    :param len_b: int
    :param k: int
    :return: the value at pth percentile
    """
    # print("k:", k)
    left = 0
    right = len_a
    while left < right:
        m1 = left + (right - left) // 2  # divide the array into two halves
        m2 = k - m1  # the separator for b is naturally to take m1 from k
        if a[m1] < b[m2 - 1]:
            left = m1 + 1
        else:
            right = m1

        # print("m1", m1, "m2", m2, "left", left, "right", right)

    m1 = left
    m2 = k - m1
    # print("m1", m1, "m2", m2)
    return max(a[m1 - 1] if m1 > 0 else float("-inf"), b[m2 - 1] if m2 > 0 else float("-inf"))


def find_percentile(a, b, p):
    len_a = len(a)
    len_b = len(b)
    # print("array a:", len_a, a)
    # print("array b:", len_b, b)
    # print("sorted:", sorted(a + b))
    idx = math.ceil(p * (len_a + len_b) / 100)
    # print("Index", idx-1, "Answer:", sorted(a + b)[idx-1])

    if len_a < len_b:
        return find_percentile_base(a, b, len_a, idx)
    else:
        return find_percentile_base(b, a, len_b, idx)


def test_find_percentile(a, b, p, correct_answer):
    assert find_percentile(a, b, p) == correct_answer


def run_unit_tests():
    from numpy.random import seed
    from numpy.random import randint

    p = 50
    seed(7)
    a = sorted(randint(100, size=10))
    b = sorted(randint(100, size=100))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx-1])

    seed(11)
    a = sorted(randint(100, size=7))
    b = sorted(randint(100, size=100))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    seed(13)
    a = sorted(randint(100, size=7))
    b = sorted(randint(100, size=100))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    p = 73
    seed(17)
    a = sorted(randint(100, size=27))
    b = sorted(randint(100, size=3))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    seed(29)
    a = sorted(randint(100, size=99))
    b = sorted(randint(100, size=77))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    p = 73
    seed(31)
    a = sorted(randint(100, size=5))
    b = sorted(randint(100, size=7))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])


def run_stress_test():
    from numpy.random import seed
    from numpy.random import randint
    from datetime import datetime

    p = 50
    seed(datetime.now().microsecond)
    a = sorted(randint(100, size=10))
    b = sorted(randint(100, size=100))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    seed(datetime.now().microsecond)
    a = sorted(randint(100, size=31))
    b = sorted(randint(100, size=100))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    seed(datetime.now().microsecond)
    a = sorted(randint(100, size=7))
    b = sorted(randint(100, size=103))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    p = 73
    seed(datetime.now().microsecond)
    a = sorted(randint(100, size=27))
    b = sorted(randint(100, size=7))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    seed(datetime.now().microsecond)
    a = sorted(randint(100, size=99))
    b = sorted(randint(100, size=77))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])

    p = 73
    seed(datetime.now().microsecond)
    a = sorted(randint(100, size=5))
    b = sorted(randint(100, size=7))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    test_find_percentile(a, b, p, sorted(a + b)[idx - 1])


# find_percentile works 10 seconds on the max test
def run_max_test():
    from numpy.random import seed
    from numpy.random import randint
    from datetime import datetime

    p = randint(100)
    seed(datetime.now().microsecond)
    max_size = 150000
    a = sorted(randint(2**16, size=max_size))
    b = sorted(randint(2**16, size=max_size))
    idx = math.ceil(p * (len(a) + len(b)) / 100)
    ans = sorted(a + b)[idx - 1]

    start = time.time()
    test_find_percentile(a, b, p, ans)
    end = time.time()
    print("Max test took: ", end - start)


if __name__ == '__main__':
    run_unit_tests()
    run_stress_test()
    run_max_test()
