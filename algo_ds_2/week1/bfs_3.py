

def maze2graph(maze):
    height, width = len(maze), len(maze[0])
    # print(height, width)
    # graph = {(x, y): [] for y in range(width) for x in range(height) if maze[x][y] != "#"}
    graph = {}
    for y in range(height):
        for x in range(width):
            if maze[y][x] == '#':
                continue

            graph[(y, x)] = []
            if x - 1 >= 0:
                if maze[y][x-1] in ('.', 'X'):
                    graph[(y, x)].append((y, x-1))
            if x + 1 < width:
                if maze[y][x+1] in ('.', 'X'):
                    graph[(y, x)].append((y, x+1))
            if y - 1 >= 0:
                if maze[y-1][x] in ('.', 'X'):
                    graph[(y, x)].append((y - 1, x))
            if y + 1 < height:
                if maze[y+1][x] in ('.', 'X'):
                    graph[(y, x)].append((y + 1, x))


    return graph

maze = [
    '....#.',
    '....#.']
maze = [
    '....#.']

maze = [
    '...',
    '.#.',
    '##X']

# check that your code works correctly on provided example
# assert maze2graph(maze) == \
#        {(0, 0): [(0, 1)], (0, 1): [(0, 0), (0, 2)], (0, 2): [(0, 1), (0, 3)], (0, 3): [(0, 2)], (0, 5): []}, 'Wrong answer'


ans = {(0, 0): [(1, 0), (0, 1)], (1, 0): [(0, 0)], (0, 1): [(0, 0), (0, 2)], (0, 2): [(1, 2), (0, 1)], (1, 2): [(0, 2), (2, 2)], (2, 2): [(1, 2)]}

my = maze2graph(maze)

for k, _ in my.items():
    if k not in ans:
        print("extra key", k)

for k, v in ans.items():
    if k not in my:
        print("key", k, "not in ans")
        continue

    if my[k] != v:
        print(k, v, my[k])
