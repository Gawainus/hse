n = int(input())

if n == 0:
    print(0)
elif n < 2:
    print(1)
else:
    fib_n_2 = 1
    fib_n_1 = 1

    i = 3
    while True:
        fib = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1
        fib_n_1 = fib

        if fib > n:
            print("-1")
            break
        elif fib == n:
            print(i)
            break

        i += 1


