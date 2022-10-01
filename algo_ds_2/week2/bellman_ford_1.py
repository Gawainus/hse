

def BellmanFord(weight_matrix, v_from):
    n, graph = len(weight_matrix), weight_matrix
    dist = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[v_from] = 0

    for _ in range(n):

        for i in range(n):
            for j in range(n):
                e = graph[i][j]
                if e == float('inf'):
                    continue

                cost = dist[i] + e
                if cost < dist[j]:
                    dist[j] = cost
                    prev[j] = i

    return dist



weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), float('inf')],
                 [2, float('inf'), float('inf')]]
v_from = 0
# check that your code works correctly on provided example
assert BellmanFord(weight_matrix, v_from) == [0, 5, 2], 'Wrong answer'
