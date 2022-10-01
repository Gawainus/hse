import json

N = int(input())

d = dict()
for _ in range(0, N):
    s = input()
    ini = s[0]
    if ini not in d:
        d[ini] = dict()

    ini2 = s[:2]
    if ini2 not in d[ini]:
        d[ini][ini2] = list()

    d[ini][ini2].append(s)

    for v in d.values():
        for k, v2 in v.items():
            v[k] = sorted(v2)

o_file = input()
with open(o_file, 'w') as f:
    f.write(json.dumps(d))
