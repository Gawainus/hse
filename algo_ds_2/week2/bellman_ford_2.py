def hasNegativeCycle(weight_matrix):
    def bellman_ford(n, graph, source):
        dist = [float("inf") for _ in range(n)]
        prev = [None for _ in range(n)]
        dist[source] = 0

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

        for i in range(n):
            for j in range(i, n):
                e = graph[i][j]
                if e == float('inf'):
                    continue

                cost = dist[i] + e
                if cost < dist[j]:
                    return True

        return False

    n, graph = len(weight_matrix), weight_matrix
    for s in range(n):
        neg = bellman_ford(n, graph, s)
        if neg:
            return True

    return False


weight_matrix = [[float('inf'), 5, 2],
                 [5, float('inf'), -10],
                 [2, -10, float('inf')]]
# check that your code works correctly on provided example
assert hasNegativeCycle(weight_matrix), 'Wrong answer'
