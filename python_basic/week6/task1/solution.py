a = float(input())
b = float(input())
op = input()


def calc(a, b, op):
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    else:
        print(a / b)


calc(a, b, op)