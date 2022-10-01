# def teamOracle(team_size, start_times, finish_times):
#     acts = list(zip(start_times, finish_times))
#     finish_sorting = lambda x: x[1]
#     acts = sorted(acts, key=finish_sorting)
#     print(acts)
#     q = []
#     for s, e in acts:
#         # check if team members have done
#         while q:
#             prev_finish = q[0][1]
#             if s >= prev_finish:
#                 q.pop(0)
#                 team_size += 1
#             else:
#                 break
#
#         if team_size > 0:
#             q.append((s, e))
#             team_size -= 1
#         else:
#             print("start_time", s, "team_size", team_size)
#             return False
#
#         print(team_size)
#     return True


def teamOracle(team_size, start_times, finish_times):
    s = min(start_times)
    e = max(finish_times)
    length = e + 1
    m = [[0] * length for _ in range(len(start_times))]
    for i, (s, e) in enumerate(zip(start_times, finish_times)):
        for j in range(s, e + 1):
            m[i][j] = 1

    for j in range(length):
        c = 0
        for i in range(len(start_times)):
            if m[i][j] == 1:
                c += 1

        if c > team_size:
            return False

    return True


team_size = 4
start_times = [1, 5, 10]
finish_times = [3, 7, 15]
assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'
#
#
# team_size = 4
# start_times = [1, 5, 10]
# finish_times = [6, 7, 15]
# assert teamOracle(team_size, start_times, finish_times), 'Wrong answer'
#
# team_size = 2
# start_times = [1, 5, 10]
# finish_times = [14, 13, 15]
# assert not teamOracle(team_size, start_times, finish_times), 'Wrong answer'
#

team_size = 9
start_times = [6, 10, 3, 1, 10, 1, 6, 20, 1, 12, 5, 1, 5, 6, 5, 7, 1, 13]
finish_times = [11, 15, 18, 19, 17, 10, 16, 21, 1, 21, 9, 10, 10, 11, 6, 11, 19, 15]
assert not teamOracle(team_size, start_times, finish_times), 'Wrong answer'
