def minUnionCost(set_sizes):
    import heapq
    heapq.heapify(set_sizes)
    min_sum = 0
    while len(set_sizes) > 1:
        s1 = heapq.heappop(set_sizes)
        s2 = heapq.heappop(set_sizes)
        c = s1 + s2
        min_sum += c
        heapq.heappush(set_sizes, c)

    return min_sum


set_sizes = [2, 6]
assert minUnionCost(set_sizes) == 8, 'Wrong answer'

set_sizes = [1, 2, 3, 4, 5]
assert minUnionCost(set_sizes) == 33, 'Wrong answer'
