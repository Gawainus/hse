a1 = input().split()
a2 = map(float, input().split())
a = zip(a1, a2)
a = filter(lambda x: x[1] > 0.5, a)
a = sorted(a, key=lambda x: x[1], reverse=True)
print("\n".join(list(zip(*a))[0]))
