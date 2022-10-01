graph = []
visited = []


def dfs(v):
    # MODIFY THIS FUNCTION
    visited[v] = True
    vertex_count = 0
    for j, u in enumerate(graph[v]):
        if not visited[j] and u:
            vertex_count += 1 + dfs(j)

    return vertex_count

def sameComponent(adj_matrix, vertex):
    global graph, visited
    graph = adj_matrix
    n = len(graph)
    visited = [False for i in range(n)]
    vertex_count = 1

    # YOUR CODE GOES HERE
    vertex_count += dfs(vertex)

    return vertex_count


adj_matrix = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0]]
print(sameComponent(adj_matrix, 1))
print(sameComponent(adj_matrix, 1))
print(sameComponent(adj_matrix, 1))
