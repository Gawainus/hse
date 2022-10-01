from heapq import heappop, heappush


def dijkstraPath(adj_matrix, v_from, v_to):
    n, graph = len(adj_matrix), adj_matrix
    heap = []
    visited = [False for _ in range(n)]
    prev = [-1 for _ in range(n)]
    dists = [float('inf') for i in range(n)]
    dists[v_from] = 0
    heappush(heap, (dists[v_from], v_from))
    while heap:
        d, curr = heappop(heap)
        visited[curr] = True

        for n, c in enumerate(adj_matrix[curr]):
            if visited[n]:
                continue

            curr_cost = dists[curr] + c
            if curr_cost < dists[n]:
                dists[n] = curr_cost
                prev[n] = curr
                heappush(heap, (dists[n], n))

    path = [v_to]
    if v_to == v_from:
        return path

    curr = v_to
    for _ in range(len(prev)):
        curr = prev[curr]
        if curr == -1:
            return -1

        path.append(curr)
        if curr == v_from:
            break

    return path[::-1]


adj_matrix = [[float('inf'), 5, 2],
              [5, float('inf'), float('inf')],
              [2, float('inf'), float('inf')]]
v_from, v_to = 0, 2
assert dijkstraPath(adj_matrix, v_from, v_to) == [0, 2], 'Wrong answer'

adj_matrix = [[float('inf'), 4, float('inf'), float('inf'), float('inf'), float('inf'), 7, float('inf'), float('inf')],
              [4, float('inf'), 9, float('inf'), float('inf'), float('inf'), 11, 20, float('inf')],
              [float('inf'), 9, float('inf'), 6, 2, float('inf'), float('inf'), float('inf'), float('inf')],
              [float('inf'), float('inf'), 6, float('inf'), 10, 5, float('inf'), float('inf'), float('inf')],
              [float('inf'), float('inf'), 2, 10, float('inf'), 15, float('inf'), 1, 5],
              [float('inf'), float('inf'), float('inf'), 5, 15, float('inf'), float('inf'), float('inf'), 12],
              [7, 11, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf')],
              [float('inf'), 20, float('inf'), float('inf'), 1, float('inf'), 1, float('inf'), 3],
              [float('inf'), float('inf'), float('inf'), float('inf'), 5, 12, float('inf'), 3, float('inf')]]

print(dijkstraPath(adj_matrix, v_from, v_to))


adj_matrix = [[float('inf'), 5, 2, float('inf')],
              [5, float('inf'), float('inf'), float('inf')],
              [2, float('inf'), float('inf'), float('inf')],
              [float('inf'), float('inf'), float('inf'), float('inf')]]

v_from, v_to = 3, 0
print(dijkstraPath(adj_matrix, v_from, v_to))


adj_matrix = [[float('inf'), 2, 1, float('inf'), float('inf')],
              [2, float('inf'), float('inf'), float('inf'), 2],
              [1, float('inf'), float('inf'), float('inf'), 2],
              [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
              [float('inf'), 2, 2, float('inf'), float('inf')]]

v_from, v_to = 0, 4
print(dijkstraPath(adj_matrix, v_from, v_to))

adj_matrix = [[0, 2, 1, float('inf'), float('inf')],
              [2, float('inf'), float('inf'), float('inf'), 2],
              [1, float('inf'), float('inf'), float('inf'), 2],
              [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
              [float('inf'), 2, 2, float('inf'), float('inf')],
    ]

v_from, v_to = 0, 0
print(dijkstraPath(adj_matrix, v_from, v_to))

v_from, v_to = 0, 1
print(dijkstraPath(adj_matrix, v_from, v_to))
