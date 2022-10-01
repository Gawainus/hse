def _partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def partition(array, pivot_index):
    high = len(array) - 1
    array[high], array[pivot_index] = array[pivot_index], array[high]
    _partition(array, 0, high)
    return array


arr = [3, 2, 1, 4]
pivot_index = 0
print(partition(arr, pivot_index))

assert partition(arr, pivot_index) in [[1, 2, 3, 4], [2, 1, 3, 4]], 'Wrong answer'
