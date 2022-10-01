class Deque:

    def __init__(self):
        self.front = []
        self.back = []
        self.size = 0

    def push_front(self, key):
        self.front.append(key)
        self.size += 1
        return "ok"

    def push_back(self, key):
        self.back.append(key)
        self.size += 1
        return "ok"

    def pop_front(self):
        if self.size == 0:
            return "error"

        self.size -= 1

        if not self.front:
            ret = self.back[0]
            self.back = self.back[1:]
            return ret

        return self.front.pop()

    def pop_back(self):
        if self.size == 0:
            return "error"

        self.size -= 1
        if not self.back:
            ret = self.front[0]
            self.front = self.front[1:]
            return ret

        return self.back.pop()

    def front(self):
        if self.size == 0:
            return "error"

        if self.front:
            return self.front[-1]
        else:
            return self.back[0]

    def back(self):
        if self.size == 0:
            return "error"

        if self.back:
            return self.back[-1]
        else:
            return self.front[0]

    def clear(self):
        self.front.clear()
        self.back.clear()
        self.size = 0
        return "ok"

    def size(self):
        return self.size


def process_deque(commands):
    d = Deque()
    ret = []
    for c in commands:
        if 'push' in c:
            cmd, key = c.split()
            func = getattr(Deque, cmd)
            ret.append(func(d, key))
        else:
            func = getattr(Deque, c)
            ret.append(func(d))

    return ret


if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))
