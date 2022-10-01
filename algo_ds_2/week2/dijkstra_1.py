from heapq import heappop, heappush


def dijkstra(adj_matrix, v_from, v_to):
    n, graph = len(adj_matrix), adj_matrix
    heap = []
    visited = [False for i in range(n)]
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

    return -1 if dists[v_to] == float('inf') else dists[v_to]


adj_matrix = [[float('inf'), 5, 2],
              [5, float('inf'), float('inf')],
              [2, float('inf'), float('inf')]]

v_from, v_to = 0, 2
# check that your code works correctly on provided example
assert dijkstra(adj_matrix, v_from, v_to) == 2, 'Wrong answer'

adj_matrix = [[float('inf'), 5, 2, float('inf')],
              [5, float('inf'), float('inf'), float('inf')],
              [2, float('inf'), float('inf'), float('inf')],
              [2, float('inf'), float('inf'), float('inf')]]

v_from, v_to = 0, 2
assert dijkstra(adj_matrix, v_from, v_to) == 2, 'Wrong answer'

v_from, v_to = 0, 3
assert dijkstra(adj_matrix, v_from, v_to) == -1, 'Wrong answer'

adj_matrix = [
    [float('inf'), 4, float('inf'), float('inf'), float('inf'), float('inf'), 7, float('inf'), float('inf')],
    [4, float('inf'), 9, float('inf'), float('inf'), float('inf'), 11, 20, float('inf')],
    [float('inf'), 9, float('inf'), 6, 2, float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 6, float('inf'), 10, 5, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 2, 10, float('inf'), 15, float('inf'), 1, 5],
    [float('inf'), float('inf'), float('inf'), 5, 15, float('inf'), float('inf'), float('inf'), 12],
    [7, 11, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf')],
    [float('inf'), 20, float('inf'), float('inf'), 1, float('inf'), 1, float('inf'), 3],
    [float('inf'), float('inf'), float('inf'), float('inf'), 5, 12, float('inf'), 3, float('inf')]]

v_from, v_to = 0, 3
print(dijkstra(adj_matrix, v_from, v_to))

v_from, v_to = 0, 2
print(dijkstra(adj_matrix, v_from, v_to))
