d = dict()


def is_palindrome(s, j, i):
    if j == i:
        d[(j, i)] = True
        return True

    if j + 1 == i:
        r = s[i] == s[j]
        d[(j, i)] = r
        return r

    k = (j + 1, i - 1)
    r = d[k] and (s[i] == s[j])
    d[(j, i)] = r
    return r


def largest_palindrome(s):
    m = ''
    for i in range(len(s)):
        for j in range(0, i+1):
            sub = s[j:i+1]
            if is_palindrome(s, j, i) and len(sub) > len(m):
                m = sub

    return m


# print(largest_palindrome('ABCBC'))
