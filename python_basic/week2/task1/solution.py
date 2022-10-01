"""
According to the Gregorian calendar,
a year is a leap year if its number is a multiple of 4
but not a multiple of 100, or if it is a multiple of 400.


"""
y = input()
y = int(y)
is_leap = ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)

if is_leap:
    print("YES")
else:
    print("NO")