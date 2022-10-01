import math


def all_paths(maze, i=0, j=0):
    def inner(maze, content, n, m, i, j):
        if i == n - 1 and j == m - 1:
            return [(1, [(i, j)])]

        sol = []
        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= a < n and 0 <= b < m and (a, b) not in content:
                k = a, b
                content.add(k)
                tails = inner(maze, content, a, b)
                for length, t in tails:
                    t.append((i, j))
                    sol.append((length + 1, t))

                content.remove(k)

        if not sol:
            return [(1, [(i, j)])]

        return sol

    n = len(maze)
    m = len(maze[0])
    sol = inner(maze, {(i, j)}, n, m, i, j)
    print(len(sol))
    for i, (l, s) in enumerate(sol):
        print(i, l, s[::-1])

def fastest_escape_length(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1

    maze[i][j] = 1
    result = math.inf
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            result = min(result, fastest_escape_length(maze, a, b) + 1)

    maze[i][j] = 0
    return result


def fastest_escapes(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    def inner(maze, n, m, i, j):
        if i == n - 1 and j == m - 1:
            return [[(i, j)]]

        maze[i][j] = 1
        sol = []
        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
                tails = inner(maze, n, m, a, b)
                for t in tails:
                    if len(t) > 0:
                        t.append((i, j))
                        sol.append(t)

        maze[i][j] = 0
        return sol

    n = len(maze)
    m = len(maze[0])
    sol = inner(maze, n, m, i, j)
    shortest = math.inf
    for s in sol:
        shortest = min(shortest, len(s))

    out_arr = []
    for s in sol:
        if len(s) == shortest:
            out_arr.append(s[::-1])
    return out_arr


def weighted_escape_length(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    def inner(maze, content, i, j):
        if i == n - 1 and j == m - 1:
            return [(1, [(i, j)])]

        sol = []
        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= a < n and 0 <= b < m and (a, b) not in content:
                k = a, b
                content.add(k)
                tails = inner(maze, content, a, b)
                for length, t in tails:
                    t.append((i, j))
                    cost = w if maze[a][b] > 0 else 1
                    sol.append((length + cost, t))

                content.remove(k)

        if not sol:
            return [(1, [(i, j)])]

        return sol

    sol = inner(maze, {(i, j)}, i, j)
    # print(len(sol))
    cheapest = math.inf
    for i, (l, s) in enumerate(sol):
        r = s[::-1]
        # print(i, l, r)
        if l < cheapest and r[-1] == (n-1, m-1):
            cheapest = l

    return cheapest


def weighted_escapes(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])

    def inner(maze, content, i, j):
        if i == n - 1 and j == m - 1:
            return [(1, [(i, j)])]

        sol = []
        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= a < n and 0 <= b < m and (a, b) not in content:
                k = a, b
                content.add(k)
                tails = inner(maze, content, a, b)
                for length, t in tails:
                    t.append((i, j))
                    cost = w if maze[a][b] > 0 else 1
                    sol.append((length + cost, t))

                content.remove(k)

        if not sol:
            return [(1, [(i, j)])]

        return sol

    sol = inner(maze, {(i, j)}, i, j)
    # print(len(sol))
    cheapest = math.inf
    for i, (l, s) in enumerate(sol):
        r = s[::-1]
        # print(i, l, r)
        if l < cheapest and r[-1] == (n-1, m-1):
            cheapest = l

    out_arr = []
    for l, s in sol:
        r = s[::-1]
        if l == cheapest and r[-1] == (n-1, m-1):
            out_arr.append(r)

    return out_arr


# some test code
if __name__ == "__main__":
    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # # should print 5
    # print(fastest_escape_length(test_a))

    # # should print 2
    # print(weighted_escape_length(test_a, 0))
    # print(all_paths(test_a))
    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # # should print inf
    # print(fastest_escape_length(test_b))
    # # should print 5
    # print(weighted_escape_length(test_b, 1))
    # # should print 6
    # print(weighted_escape_length(test_b, 2))
    #

    # should print [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # print(fastest_escapes(test_a))
    # should print []
    # print(fastest_escapes(test_b))
    # should print [5, 5, 5, 5, 5, 5]
    # print(list(map(len, fastest_escapes([[0 for _ in range(3)] for _ in range(3)]))))

    # # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
    # print(weighted_escapes(test_b, 0))
    # # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # # the order of the paths within the list might be different
    # print(weighted_escapes(test_b, 2))

    # test_c = [
    #     [0, 0, 0],
    #     [1, 1, 1],
    #     [0, 0, 0]
    # ]
    test_c = [
        [0],
    ]
    print(weighted_escapes(test_c, 2))
