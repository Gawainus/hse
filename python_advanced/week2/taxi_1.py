dists = sorted([int(i) for i in input().split()])
fares = sorted([int(i) for i in input().split()], key=None, reverse=True)

print(sum([d * f for d, f in zip(dists, fares)]))
