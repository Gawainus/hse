import math


class Node:
    def __init__(self, key=0, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def insert(root, node):
    if root.key > node.key:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)


#######################################################

def count_distinct(root):
    d = set()

    def inner(root):
        distinct = 0
        if not root:
            return distinct

        if root.key not in d:
            d.add(root.key)
            distinct = 1

        return distinct + inner(root.left) + inner(root.right)

    return inner(root)


def tree_max(root):
    ret = - math.inf
    if root:
        ret = max(ret, root.key)
    else:
        return ret

    ret = max([ret, tree_max(root.left), tree_max(root.right)])
    return ret


def _check_BST(root):
    if not root:
        return True

    if not root.left and not root.right:
        return True

    if not root.left:
        return _check_BST(root.right)

    if not root.right:
        return _check_BST(root.left)

    if root.left.key > root.right.key:
        return False
    return _check_BST(root.left) and _check_BST(root.right)


def check_BST(root):
    return _check_BST(root)


def _min_diff(root):
    if not root:
        return math.inf

    left_diff = math.inf
    right_diff = math.inf
    if root.left:
        left_diff = abs(root.key - root.left.key)

    if root.right:
        right_diff = abs(root.key - root.right.key)

    return min([left_diff, right_diff, _min_diff(root.left), _min_diff(root.right)])


def min_diff(root):
    return _min_diff(root)


#################################################

if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(1))
    insert(T, Node(2))

    # print(tree_max(T))

    # # should print True
    # print(check_BST(T))

    # # should print 1
    print(min_diff(T))

    # print(count_distinct(T))
