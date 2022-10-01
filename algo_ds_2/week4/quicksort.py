def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def _quick_sort(array, low, high):
    if low >= high:
        return

    pi = partition(array, low, high)
    _quick_sort(array, low, pi - 1)
    _quick_sort(array, pi + 1, high)


def quicksort(array):
    n = len(array)
    _quick_sort(array, 0, n - 1)
    return array


arr = [3, 2, 1, 4]
# check that your code works correctly on provided example
assert quicksort(arr) == [1, 2, 3, 4], 'Wrong answer'
