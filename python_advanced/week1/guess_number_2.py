N = int(input())

ans = set()


def parseNums(d):
    return set(d.split())


counter = 0
ans = None
ans_prev = set()
while True:
    d = input()
    if d == "HELP":
        break

    if counter % 2 == 0:
        num_set = parseNums(d)
    else:
        if d == "YES":
            if ans is None:
                ans = num_set
            else:
                ans.update(num_set.intersection(ans_prev))
                ans_prev = num_set
        else:
            ans.difference_update(num_set)

    counter += 1

ans = [int(i) for i in ans]

s = ""
for i in sorted(ans):
    s += f"{i} "

print(s)
