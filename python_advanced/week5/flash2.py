class FlashError(Exception):
    pass


class FlashMaxFileSizeError(FlashError):
    pass


class FlashMemoryLimitError(FlashError):
    pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.max_file_size = max_file_size
        self.size = 0

    def write(self, v):
        if self.max_file_size and v > self.max_file_size:
            raise FlashMaxFileSizeError

        if self.size + v <= self.capacity:
            self.size += v
        else:
            raise FlashMemoryLimitError(
                f"Only {self.capacity - self.size} left.")
