
def countingsort(array, lowerbound, upperbound):
    """
    :param array:
    :param lowerbound:
    :param upperbound:
    :return:
    """

    if not array:
        return []

    count = [0 for _ in range(lowerbound, upperbound + 1)]
    sorted_array = [0 for _ in range(len(array))]

    for i in array:
        count[i - lowerbound] += 1

    idx = 0
    for i, c in enumerate(count):
        while c > 0:
            sorted_array[idx] = i + lowerbound
            c -= 1
            idx += 1

    return sorted_array


arr = [3, 2, 1]
lowerbound = 1
upperbound = 3
assert countingsort(arr, lowerbound, upperbound) == sorted(arr), 'Wrong answer'

arr = []
lowerbound = 0
upperbound = 10
assert countingsort(arr, lowerbound, upperbound) == sorted(arr), 'Wrong answer'

arr = [5, 2]
lowerbound = 2
upperbound = 5
assert countingsort(arr, lowerbound, upperbound) == sorted(arr), 'Wrong answer'

arr = [1, 4, 1, 2, 7, 5, 2]
lowerbound = min(arr)
upperbound = max(arr)
assert countingsort(arr, lowerbound, upperbound) == sorted(arr), 'Wrong answer'

from random import randint
arr = [randint(7, 127) for i in range(100)]
lowerbound = min(arr)
upperbound = max(arr)
assert countingsort(arr, lowerbound, upperbound) == sorted(arr), 'Wrong answer'

arr = [randint(56, 999) for i in range(100)]
lowerbound = min(arr)
upperbound = max(arr)
assert countingsort(arr, lowerbound, upperbound) == sorted(arr), 'Wrong answer'
