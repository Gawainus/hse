dists = input().split()
N = len(dists)

dists = sorted(zip(range(N), map(int, dists)), key=lambda x: x[1])
fares = sorted(zip(range(N),  map(int, input().split())),
               key=lambda x: x[1],
               reverse=True)

dists = map(lambda x: x[0], dists)
fares = map(lambda x: x[0], fares)

indices = sorted(zip(dists, fares), key=lambda x: x[0])
indices = map(lambda x: str(x[1]), indices)
print(' '.join(indices))
