def longestNonRepeating(text):
    n = len(text)
    longest = 0

    chs = set()
    i = 0
    for j in range(n):
        c = text[j]
        if c not in chs:
            chs.add(c)
            longest = max(longest, j - i + 1)
            continue

        while i <= j:
            t = text[i]
            chs.discard(t)
            i += 1
            if c not in chs:
                chs.add(c)
                longest = max(longest, j - i + 1)
                break

    return longest


# text = 'ba'
# assert longestNonRepeating(text) == 2, 'Wrong answer'
#
# text = 'baa'
# assert longestNonRepeating(text) == 2, 'Wrong answer'

text = 'ababa'
# assert longestNonRepeating(text) == 2, 'Wrong answer'
print(longestNonRepeating(text))
