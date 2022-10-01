N = int(input())

w_to_stress = dict()
for _ in range(N):
    w = input()
    if w.lower() not in w_to_stress:
        w_to_stress[w.lower()] = []

    w_to_stress[w.lower()].append(w)

words = input().split()

count = 0
for w in words:
    if (w.lower() not in w_to_stress) \
            and (sum(1 for c in w if c.isupper()) != 1):
        count += 1

    if w.lower() in w_to_stress:
        chain = w_to_stress[w.lower()]

        found = False
        for candi in chain:
            if candi == w:
                found = True
                break

        if not found:
            count += 1

print(count)
