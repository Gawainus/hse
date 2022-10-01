def isAnagram(string1, string2):
    if len(string1) != len(string2):
        return False

    def parse_str(str):
        d = {}
        for c in str:
            if c not in d:
                d[c] = 0

            d[c] += 1

        return d

    d1 = parse_str(string1)
    d2 = parse_str(string2)

    return d1 == d2

string1 = 'baa'
string2 = 'aab'
assert isAnagram(string1, string2), 'Wrong answer'

string1 = 'listen'
string2 = 'silent'
assert isAnagram(string1, string2), 'Wrong answer'
