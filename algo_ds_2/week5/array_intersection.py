def arrayIntersection(array1, array2):
    intersection = []

    def parse_arr(arr):
        d = {}
        for e in arr:
            if e not in d:
                d[e] = 0

            d[e] += 1

        return d

    d1 = parse_arr(array1)
    d2 = parse_arr(array2)
    for k in d1.keys():
        if k in d2:
            intersection.extend([k] * min(d1[k], d2[k]))

    return intersection


array1 = [1, 2, 3]
array2 = [2, 4, 5]
assert arrayIntersection(array1, array2) == [2], 'Wrong answer'

array1 = [1, 2, 3, 2]
array2 = [2, 4, 5, 4, 2]
assert arrayIntersection(array1, array2) == [2, 2], 'Wrong answer'
