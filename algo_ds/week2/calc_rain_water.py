# def calc_rain_water(h):
#     if not h:
#         return 0
#
#     size = len(h)
#     s = 0
#     for i, b in enumerate(h):
#         left = 0
#         right = 0
#         for j in range(i, -1, -1):
#             left = max(left, h[j])
#         for j in range(i, size):
#             right = max(right, h[j])
#
#         tall = min(left, right)
#         height = tall - b
#         # print(left, right, tall, b)
#         # if height > 0:
#         s += height
#
#     return s

def calc_rain_water(h):
    if not h:
        return 0

    size = len(h)
    left_max = [0] * size
    max_so_far = 0
    for i, b in enumerate(h):
        left_max[i] = max(max_so_far, b)
        max_so_far = left_max[i]

    right_max = [0] * size
    max_so_far = 0
    for i, b in enumerate(h[::-1]):
        right_max[i] = max(max_so_far, b)
        max_so_far = right_max[i]

    right_max = right_max[::-1]

    s = 0
    for i, b in enumerate(h):
        tall = min(left_max[i], right_max[i])
        height = tall - b
        s += height

    return s


# some test code
if __name__ == "__main__":
    test_h = [2, 5, 2, 3, 6, 9, 1, 3, 4, 6, 1]
    # should print 15
    print(calc_rain_water(test_h))

    test_h = [2, 4, 6, 8, 6, 4, 2]
    # should print 0
    print(calc_rain_water(test_h))

    test_h = [8, 6, 4, 2, 4, 6, 8]
    # should print 18
    print(calc_rain_water(test_h))
