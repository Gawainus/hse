
def poly_hash(p, q, s, ):
    h = 0
    for i, c in enumerate(s):
        h += ord(c) * p ** i

    return h % q


def RabinKarp(text, pattern):
    p = 31
    q = 10 ** 9 + 7
    lt = len(text)
    lp = len(pattern)
    hpattern = poly_hash(p, q, pattern)
    indices = []
    for i in range(lt - lp + 1):
        sub = text[i:i+lp]
        h = poly_hash(p, q, sub)
        if h == hpattern and sub == pattern:
            indices.append(i)

    return indices


text = 'abracadabra'
pattern = 'ab'
# check that your code works correctly on provided example
print(RabinKarp(text, pattern))
# assert RabinKarp(text, pattern) == [0, 7], 'Wrong answer'
