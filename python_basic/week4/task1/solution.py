s = input()

parts = s.split(' ')

o = ""
for i, e in enumerate(parts):
    if i % 2 == 0:
        o += f"{e} "

print(o)
