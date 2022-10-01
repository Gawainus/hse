
s = ""
while True:
    ln = input()
    ln = ln.strip()
    if len(ln) == 0:
        break

    s += " " + ln

w_to_c = dict()
counts = []
for w in s.split():

    if w not in w_to_c:
        counts.append(0)
        w_to_c[w] = 1
    else:
        counts.append(w_to_c[w])
        w_to_c[w] += 1


s = ""
for c in counts:
    s += f"{c} "

print(s)
