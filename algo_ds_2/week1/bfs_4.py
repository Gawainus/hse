from queue import Queue


class Node:
    def __init__(self, y, x, dist, sol):
        self.y = y
        self.x = x
        self.dist = dist
        self.sol = sol


def path2exit(maze, x, y):
    height = len(maze)
    width = len(maze[0])
    # print(height, width)

    visited = [[False for _ in range(width)] for _ in range(height)]
    q = Queue()
    solutions = []
    q.put(Node(y, x, 0, ""))
    while not q.empty():
        node = q.get()
        j = node.y
        i = node.x
        dist = node.dist
        sol = node.sol
        visited[j][i] = True

        # print(j, i, maze[y][x], sol)
        if maze[j][i] == '#':
            continue

        if maze[j][i] == 'X':
            solutions.append(sol)
            continue

        if i - 1 > 0:
            if not visited[j][i-1]:
                q.put(Node(j, i-1, dist + 1, sol + "L"))
        if i + 1 < width:
            if not visited[j][i+1]:
                q.put(Node(j, i+1, dist + 1, sol + "R"))
        if j - 1 > 0:
            if not visited[j-1][i]:
                q.put(Node(j-1, i, dist + 1, sol + "U"))
        if j + 1 < height:
            if not visited[j+1][i]:
                q.put(Node(j+1, i, dist + 1, sol + "D"))

    # print(solutions)
    if not solutions:
        return -1

    shortest = len(solutions[0])
    for i, s in enumerate(solutions):
        if len(s) < shortest:
            shortest = i

    return solutions[i]

maze = [
    '..#.',
    '..#.',
    '...X',]

# maze = ['..X']

print(path2exit(maze, 0, 0))
