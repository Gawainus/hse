class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.mem = []

    def add(self, *a):
        for i in a:
            self.mem.append(i)
            self.size += 1

            if self.size >= self.maxsize:
                print(sum(self.mem))
                self.mem = []
                self.size = 0

    def get_current_part(self):
        return self.mem


# buf = Buffer(maxsize=5)
# buf.add(1, 2, 3)
# print(buf.get_current_part())  # return [1, 2, 3]
# buf.add(4, 5, 6)  # print(15) – print sum of elements [1, 2, 3, 4, 5]
# print(buf.get_current_part()) # return [6]
# buf.add(7, 8, 9, 10)  # print(40)
# print(buf.get_current_part())  # return []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5)
# print(buf.get_current_part()) # return [1]
