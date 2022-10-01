ip = input()

parts = ip.split('.')
if len(parts) != 4:
    print("NO")
    exit(0)

for p in parts:
    p = int(p)
    if p < 0 or p > 255:
        print("NO")
        exit(0)

print("YES")