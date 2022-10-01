n = input()
n = int(n)

h = n//3600
r = n % 3600

m = r//60
r = n % 60


print('{}:{:02d}:{:02d}'.format(h, m, r))
