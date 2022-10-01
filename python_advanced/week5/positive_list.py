class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def __init__(self):
        super().__init__()

    def append(self, e):
        if e <= 0:
            raise NonPositiveError

        super().append(e)
