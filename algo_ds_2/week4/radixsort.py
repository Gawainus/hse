
def countingsort(array, col, base):
    n = len(array)
    output = [0] * n
    count = [0] * (base + 1)
    min_base = ord('A') - 1

    for item in array: # generate Counts
        # get column letter if within string, else use dummy position of 0
        letter = ord(item[col]) - min_base if col < len(item) else 0
        count[letter] += 1

    for i in range(len(count)-1):   # Accumulate counts
        count[i + 1] += count[i]

    for item in reversed(array):
        # Get index of current letter of item at index col in count array
        letter = ord(item[col]) - min_base if col < len(item) else 0
        output[count[letter] - 1] = item
        count[letter] -= 1

    return output


def radixsort(names):
    if not names:
        return []

    max_col = len(max(names, key=len))
    base = ord('z') - ord('A') + 1
    for col in range(max_col-1, -1, -1):
        names = countingsort(names, col, base)

    return names

arr = []
assert radixsort(arr) == [], 'Wrong answer'

arr = ['Ivan', 'John', 'Anna']
assert radixsort(arr) == ['Anna', 'Ivan', 'John'], 'Wrong answer'

arr = ['Zaz', 'Ivan', 'John', 'Anna']
assert radixsort(arr) == ['Anna', 'Ivan', 'John', 'Zaz'], 'Wrong answer'
