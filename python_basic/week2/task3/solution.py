k = int(input())
m = int(input())
n = int(input())

N = n // k
if n % k != 0:
    N += 1

print(2 * m * N)

