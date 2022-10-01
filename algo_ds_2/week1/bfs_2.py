from queue import Queue


def isBipartite(adj_list):
    n = len(adj_list)

    q = Queue()
    visited = [False for _ in range(n)]
    colors = [0 for _ in range(n)]
    for i, covered in enumerate(visited):
        if not covered:
            q.put(i)

        color = 0
        while not q.empty():
            v = q.get()
            print(v)
            visited[v] = True
            colors[v] = color

            color = 0 if color == 1 else 1
            for u in adj_list[v]:
                if not visited[u]:
                    q.put(u)
                else:
                    if colors[u] == colors[v]:
                        return False

    return True


adj_list = [[], [2,3,4], [1,3], [1,2], [1]]
adj_list = [[2], [2], [0, 1]]
print(isBipartite(adj_list))
