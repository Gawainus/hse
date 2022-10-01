import json

file = input()

c_status_200 = 0
c_status_code = 0
c_status_else = 0
c_no_status = 0
c_cannot_read = 0
with open(file, 'r') as f:
    for ln in f:
        try:
            j = json.loads(ln)
        except (json.JSONDecodeError, ValueError):
            c_cannot_read += 1
            continue

        if 'status' not in j:
            c_no_status += 1
            continue

        status = j['status']
        if status == "" or status is None:
            c_no_status += 1
            continue

        try:
            status_code = int(status)
        except ValueError:
            c_status_else += 1
            continue

        if status_code == 200:
            c_status_200 += 1
        else:
            c_status_code += 1

print(c_status_200)
print(c_status_code)
print(c_status_else)
print(c_no_status)
print(c_cannot_read)
