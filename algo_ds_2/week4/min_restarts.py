
def minRestarts(m, t, no_request_times):
    min_restarts = 0
    curr = 0
    prev_nrt = 0
    for nrt in no_request_times:
        if nrt <= t + curr:
            prev_nrt = nrt
            continue
        else:
            # restart
            curr = (prev_nrt + 1)
            min_restarts += 1

    if curr + t < m:
        curr += (no_request_times[-1] + 1)
        min_restarts += 1

    if curr + t >= m:
        return min_restarts
    else:
        return -1


m = 100
t = 20
no_request_times = [50]
assert minRestarts(m, t, no_request_times) == -1, 'Wrong answer'

m = 15
t = 10
no_request_times = [9, 10]
print(minRestarts(m, t, no_request_times))

m = 91
t = 10
no_request_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76, 78, 80, 81, 83, 85, 86, 87, 88, 89, 90, 91]
print(minRestarts(m, t, no_request_times))
