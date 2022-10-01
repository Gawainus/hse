graph = []
visited = []


def dfs(stack, parent):
    if not stack:
        return True

    v = stack.pop()
    visited[v] = True
    # print("Node:", v)
    # print("stack:", stack)

    for u in graph[v]:
        if visited[u] and u != parent:
            return False

        if not visited[u]:
            stack.append(u)
            if not dfs(stack, v):
                return False

    return True


def isTree(adj_list):
    global graph, visited
    n = len(adj_list)

    graph = adj_list
    visited = [False for i in range(n)]
    stack = list()
    if len(graph) <= 1:
        return False

    stack.append(0)
    return dfs(stack, 0) and all(visited)


adj_list = [[1, 2], [0, 3], [0, 3], [2, 3]]
adj_list2 = [[1, 2], [0, 3], [0], [1, 0]]
adj_list3 = [[1, 2], [0], [0]]
adj_list4 = [[1, 2], [0, 2], [0, 1]]
adj_list5 = [[1, 2], [0, 4], [0], [0, 5], [1, 5], [3, 4]]
adj_list5 = [[], [], []]
# check that your code works correctly on provided example
# print(isTree(adj_list))
# print(isTree(adj_list2))
# print(isTree(adj_list3))
print(isTree(adj_list5))
