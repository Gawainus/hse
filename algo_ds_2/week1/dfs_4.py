
def dfs(coordinates, stack, n):

    top = stack.pop()
    for c in coordinates:
        x1, y1 = top
        x2, y2 = c

        if x1 == x2 or y1 == y2:
            stack.append(c)


def minRooksLeft(board_size, coordinates):
    # each entry in coordinates array looks like this: (x, y) - coordinates of the rook
    n = len(coordinates)
    eaten = {}
    rooks_left = n
    if rooks_left == 0:
        return 0

    stack = list()
    stack.append(coordinates[0])
    return dfs(coordinates[1:], stack, rooks_left)

board_size = 4
coordinates = [(0, 0), (0, 3), (3, 0)]
board_size = 4
coordinates = [(0, 0), (0, 3), (3, 0), (3, 3)]
#1

board_size = 4
coordinates = [(0, 0), (0, 3), (3, 0), (3, 3), (1, 1), (1, 2), (2, 1), (2, 2)]
#aswers should be 2
print(minRooksLeft(board_size, coordinates))
