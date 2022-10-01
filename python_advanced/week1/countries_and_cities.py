N = int(input())

c_to_cou = dict()
for i in range(N):
    ln = input().split()
    for c in ln[1:]:
        c_to_cou[c] = ln[0]

ans = []

M = int(input())
for i in range(M):
    ans.append(c_to_cou[input()])

for a in ans:
    print(a)
