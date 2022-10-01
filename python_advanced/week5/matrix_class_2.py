import copy


class Matrix:
    # Part 1
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self) -> str:
        def format_row(row, end):
            rl = len(row)
            if rl > 1:
                string = "\t".join(
                    map(str, row[:-1])) + "\t" + str(row[-1]) + end
            elif rl == 1:
                string = str(row[-1]) + end
            else:
                string = ""

            return string

        s = ""
        for r in self.matrix[:-1]:
            s += format_row(r, "\n")

        s += format_row(self.matrix[-1], "")
        return s

        # Part 2
    def size(self) -> tuple:
        lr = len(self.matrix)
        if lr == 0:
            return 0, 0

        lc = len(self.matrix[0])
        if lc == 0:
            return lr, 0

        return lr, lc

    def __eq__(self, other) -> bool:
        """
        other: Matrix
        """
        if self.size() != other.size():
            return False

        for i, r in enumerate(self.matrix):
            for j, e in enumerate(r):
                if e != other.matrix[i][j]:
                    return False

        return True

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], ["2", '2']])
print(m1 == m2)
