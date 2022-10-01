x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())

x_diff = x2 - x
y_diff = y2 - y

if x_diff == 0 or y_diff == 0:
    can_move = False
else:
    can_move = abs(x_diff/y_diff) == 1

if can_move:
    print("YES")
else:
    print("NO")

