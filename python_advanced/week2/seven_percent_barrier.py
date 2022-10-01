ps = list()
p_to_v = dict()
v_count = 0
input()

while True:
    ln = input()
    if ln == "VOTES:":
        break

    p_name = ln
    p_to_v[p_name] = 0
    ps.append(p_name)

while True:
    ln = input()
    if len(ln.split()) == 0:
        break

    v_count += 1
    p = ln
    p_to_v[p] += 1

for p_name in ps:
    v = p_to_v[p_name]
    if v/v_count >= 0.07:
        print(p_name)
