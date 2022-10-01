
#
while True:
    ln = input()
    if not ln:
        break

    i_c = 0
    while i_c < len(ln):

        s = ln[i_c:]
        i_s = s.find('<i>')
        if i_s == -1:
            break

        i_e = s.find('</i>', i_s)
        if i_e == -1:
            break

        print(s[i_s+3:i_e])
        i_c += i_e + 4
