

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


def minCyclicShift(original_string, shifted_string):
    n = len(original_string)
    combined = original_string + shifted_string
    z_arr = get_z_arr(combined)
    print(z_arr)

    ans = []
    for shift in z_arr:
        # shift = min(shift, n - shift)
        shift = n - shift
        recovered_l = shifted_string[-shift:] + shifted_string[:-shift]
        recovered_r = shifted_string[shift:] + shifted_string[: shift]
        # print(original_string)
        # print(recovered_l)
        # print(recovered_r)
        if recovered_l == original_string or recovered_r == original_string:
            ans.append(shift)

    if not ans:
        return -1

    return min(ans)

original_string = 'abcde'
shifted_string = 'eabcd'
print(minCyclicShift(original_string, shifted_string))
# output 1

original_string = 'abcde'
shifted_string = 'deabc'
print(minCyclicShift(original_string, shifted_string))
# output 2

original_string = 'abcdefgh'
shifted_string = 'ghabcdef'
print(minCyclicShift(original_string, shifted_string) )
# output 2

original_string = 'abcdefgh'
shifted_string = 'efghabcd'
print(minCyclicShift(original_string, shifted_string) )
# output 4

original_string = 'abcdefgh'
shifted_string = 'defghabc'
print(minCyclicShift(original_string, shifted_string) )
# output 5

original_string = 'abcdefgh'
shifted_string = 'gameover'
print(minCyclicShift(original_string, shifted_string) )
# output -1

original_string = 'abcdefghabcdefgh'
shifted_string = 'bcdefghabcdefgha'
print(minCyclicShift(original_string, shifted_string) )
# output 7

original_string = 'zabcd'
shifted_string = 'abcdz'
print(minCyclicShift(original_string, shifted_string) )
