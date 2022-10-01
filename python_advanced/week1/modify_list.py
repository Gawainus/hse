def modify_list(a):
    odds = [x for x in a if x % 2 == 1]
    for x in odds:
        a.remove(x)

    for idx, _ in enumerate(a):
        a[idx] /= 2
