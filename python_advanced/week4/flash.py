class Flash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

    def write(self, filesize):
        if self.size + filesize <= self.capacity:
            self.size += filesize
        else:
            raise ValueError(f"Only {self.capacity - self.size} left.")
