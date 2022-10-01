name_to_account = dict()


def dep(name, amt):
    if name not in name_to_account:
        name_to_account[name] = 0

    name_to_account[name] += amt


def wit(name, amt):
    if name not in name_to_account:
        name_to_account[name] = 0

    name_to_account[name] -= amt


def bal(name):
    if name in name_to_account:
        return name_to_account[name]
    else:
        return "ERROR"


def trans(n1, n2, amt):
    if n1 not in name_to_account:
        name_to_account[n1] = 0

    if n2 not in name_to_account:
        name_to_account[n2] = 0

    name_to_account[n1] -= amt
    name_to_account[n2] += amt


def inc(p):
    for k, v in name_to_account.items():
        if v > 0:
            name_to_account[k] = int(v * (1 + p / 100))


s = ""
while True:
    ln = input()
    if len(ln.split()) == 0:
        break

    ws = ln.split()
    if ws[0] == "DEPOSIT":
        dep(ws[1], int(ws[2]))
    elif ws[0] == "WITHDRAW":
        wit(ws[1], int(ws[2]))
    elif ws[0] == "BALANCE":
        s += str(bal(ws[1])) + "\n"
    elif ws[0] == "TRANSFER":
        trans(ws[1], ws[2], int(ws[3]))
    elif ws[0] == "INCOME":
        inc(int(ws[1]))

print(s)
