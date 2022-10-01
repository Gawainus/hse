

def get_z_arr(string):
    n = len(string)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r - l] == string[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z


def shortestCycle(cyclic_string):
    n = len(cyclic_string)
    z_arr = get_z_arr(cyclic_string)
    print(z_arr)

    arr = [x for x in z_arr if x > 0]
    if not arr:
        return n

    p = n - 1
    ret = None
    rep = None
    while p > 0:
        z = z_arr[p]
        if z == 0:
            p -= 1
            continue
        else:
            rep = z
            ret = z
            break

    if p < n - ret:
        return n

    if not rep:
        return n

    while p > 0:
        z = z_arr[p]
        if z < rep:
            return n
        else:
            rep = z
            p -= rep

    return ret


print(shortestCycle('ababab'))
print(shortestCycle('abcabc'))
print(shortestCycle('abc'))
print(shortestCycle('abca'))
print(shortestCycle('abcdab'))
print(shortestCycle('ababbcabab'))
print(shortestCycle('abbcabab'))
print(shortestCycle('aabbb'))
print(shortestCycle('bcbbcccbcc'))
