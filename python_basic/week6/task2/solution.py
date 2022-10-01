n = int(input())


def is_prime(n):
    if n > 1:
        divisible = False
        for i in range(2, n // 2):
            if (n % i) == 0:
                divisible = True
                break

        if divisible:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")


is_prime(n)
