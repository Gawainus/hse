dim = input()

dim = [int(i) for i in dim.split()]

m = dim[0]
n = dim[1]


matrix = []
for _ in range(m):
    row = input().split()
    matrix.append(row)

for j in range(n):
    s = ""
    for i in range(m):
        s += f"{matrix[i][j]} "

    print(s)
