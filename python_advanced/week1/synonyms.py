N = int(input())

forward = dict()
backward = dict()

for _ in range(N):
    a, b = input().split()
    forward[a] = b
    backward[b] = a

w = input()
if w in forward:
    print(forward[w])
else:
    print(backward[w])
