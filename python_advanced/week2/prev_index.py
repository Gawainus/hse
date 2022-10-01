
prev_idx = dict()
curr_idx = 0
s = ""
while True:
    ln = input()
    if len(ln.split()) == 0:
        break

    ws = ln.split()
    for w in ws:
        if w not in prev_idx:
            s += "-1 "
        else:
            s += f"{prev_idx[w]} "

        prev_idx[w] = curr_idx
        curr_idx += 1

print(s)
