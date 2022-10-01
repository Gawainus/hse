
cus = dict()
while True:
    ln = input()
    if len(ln.split()) == 0:
        break

    name, prd, num = ln.split()
    if name not in cus:
        cus[name] = dict()

    if prd not in cus[name]:
        cus[name][prd] = 0

    cus[name][prd] += int(num)

cus = sorted(cus.items())

for k, v in cus:
    print(f"{k}:")
    prds = sorted(v.items())
    for k, v in prds:
        print(f"{k} {v}")
