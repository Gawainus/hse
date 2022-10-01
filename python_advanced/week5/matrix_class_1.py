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


# m = Matrix([[1, 2], [4, 5], [7, 8]])
# m = Matrix([[1, 2, 3], [7, 8, 9], [13, 8, 9]])
# # m = Matrix([[1], [2], [3]])
# # m = Matrix([[]])
# print(repr(m.__str__()))
