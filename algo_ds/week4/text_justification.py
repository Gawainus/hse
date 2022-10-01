import math
import copy
#
# def tj_cost(L, W):
#     def inner(W, buf):
#         bl = len(buf)
#         if bl > L:
#             return math.inf
#
#         cost = (L - bl)**3
#         if not W:
#             return cost
#
#         print(cost, f"\'{buf}\'")
#         return min(
#             inner(W[1:], buf + " " + W[0]),
#             inner(W[1:], W[0]) + cost
#         )
#
#     return inner(W[1:], W[0])

#
# def tj_cost(L, W):
#     n = len(W) + 1
#     cs = [math.inf] * n
#     cs[0] = 0
#     for i in range(1, n):
#         buf = ""
#         for j in range(i, n):
#             if not buf:
#                 buf = W[j-1]
#             else:
#                 buf += f" {W[j-1]}"
#
#             bl = len(buf)
#             if bl > L:
#                 break
#
#             cost = (L - bl) ** 3
#             print(cost, buf)
#             print(cs)
#             if cs[i - 1] + cost < cs[j]:
#                 cs[j] = cs[i - 1] + cost
#
#     print(cs)
#     return cs[-2]


def tj_cost(L, W):
    n = len(W) + 1
    cs = [math.inf] * n
    cs[0] = 0
    sol = [[""]] * n
    for i in range(1, n):
        buf = ""
        for j in range(i, n):
            if not buf:
                buf = W[j - 1]
            else:
                buf += f" {W[j - 1]}"

            bl = len(buf)
            if bl > L:
                break

            cost = (L - bl) ** 3 if j != n - 1 else 0
            # cost = (L - bl) ** 3
            # print(i, j, cost, buf)
            # print(cs)
            if cs[i - 1] + cost <= cs[j]:
                cs[j] = cs[i - 1] + cost
                curr = copy.deepcopy(sol[i - 1])
                curr.append(buf)
                sol[j] = curr

    # print(sol)
    # print(sol[-1])
    return sum([(L - len(x))**3 for x in sol[-1][1:-1]])


def tj(L, W):
    n = len(W) + 1
    cs = [math.inf] * n
    cs[0] = 0
    sol = [[""]] * n
    for i in range(1, n):
        buf = ""
        for j in range(i, n):
            if not buf:
                buf = W[j - 1]
            else:
                buf += f" {W[j - 1]}"

            bl = len(buf)
            if bl > L:
                break

            cost = (L - bl) ** 3 if j != n - 1 else 0
            # cost = (L - bl) ** 3
            # print(i, j, cost, buf)
            # print(cs)
            if cs[i - 1] + cost <= cs[j]:
                cs[j] = cs[i - 1] + cost
                curr = copy.deepcopy(sol[i - 1])
                curr.append(buf)
                sol[j] = curr

    # print(cs)
    # print(sol)
    return "\n".join(sol[-1][1:])


if __name__ == "__main__":
    e1 = ["jars", "jaws", "joke", "jury", "juxtaposition"]
    e2 = ["jars", "jaws", "aswd"]
    e3 = ["jars", "jaws", "ab", "joke", "jury"]

    e = ["jars", "jaws", "jars", "jaws", "jokfe", "juxta"]
    L = 15
    print(tj_cost(L, e))
    print(tj(L, e))
    # should print 432
    # print(tj_cost(L_example, e1))
    # print(tj_cost(L_example, e2))

    # should print:
    #jars jaws
    #joke jury
    #juxtaposition
    # print(tj(L_example, e1))
    # print(tj_cost(15, e1))
    # print(tj(max([len(x) for x in e1]), e1))
    # print(tj(11, e3))
