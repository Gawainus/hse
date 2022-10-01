class Queue:
    def __init__(self):
        self.store = []
        self.out = []

    def push(self, x):
        self.store.append(x)

    def pop(self):
        if self.out:
            return self.out.pop()

        if self.store:
            self.out = self.store[::-1]
            self.store = []
            return self.out.pop()

        raise IndexError('pop from an empty queue')

# queue = Queue()
#
# queue.push(3)
# queue.push(5)
# queue.push(7)
# queue.push(9)
#
# print(queue.pop())  # return 3
# print(queue.pop())  # return 5
# print(queue.pop())  # return 7
# print(queue.pop())  # return 9
# print(queue.pop())  # IndexError('pop from an empty queue')
