n = int(input())

if n < 2:
    print(1)

fib_n_2 = 1
fib_n_1 = 1

for i in range(n-2):
    fib = fib_n_1 + fib_n_2
    fib_n_2 = fib_n_1
    fib_n_1 = fib

print(fib)

