from queue import Queue


class Node:
    def __init__(self, seq, dist):
        self.seq = seq
        self.dist = dist


def distance(adj_list, v_from, v_to):
    n = len(adj_list)
    visited = [False for i in range(n)]
    q = Queue()
    q.put(Node(v_from, 0))

    distance = -1
    while not q.empty():
        v = q.get()
        seq = v.seq
        dist = v.dist
        visited[seq] = True

        if seq == v_to:
            if distance == -1:
                distance = dist
            else:
                distance = min(dist, distance)

            continue

        for u in adj_list[seq]:
            if not visited[u]:
                q.put(Node(u, dist + 1))

    return distance


adj_list = [[1], [0, 2], [1]]
v_from, v_to = 0, 2
print(distance(adj_list, v_from, v_to))
