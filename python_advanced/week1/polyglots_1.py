N = int(input())

lang_to_count = dict()
for i in range(N):
    m = int(input())
    for j in range(m):
        ln = input()
        if ln in lang_to_count:
            lang_to_count[ln] += 1
        else:
            lang_to_count[ln] = 1

ans = []
for k, v in lang_to_count.items():
    if v == N:
        ans.append(k)

print(len(ans))
for ln in sorted(ans):
    print(ln)
