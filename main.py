import string


def hex(red, green, blue):
    r = int(red / 16)
    if r >= 10:
        r = chr(r - 10 + ord('a'))
    r2 = red % 16
    if r2 >= 10:
        r2 = chr(r2 - 10 + ord('a'))

    b = int(blue / 16)
    if b >= 10:
        b = chr(b - 10 + ord('a'))
    b2 = red % 16
    if b2 >= 10:
        b2 = chr(b2 - 10 + ord('a'))

    c = int(green / 16)
    if c >= 10:
        c = chr(c - 10 + ord('a'))
    c2 = green % 16
    if c2 >= 10:
        c2 = chr(c2 - 10 + ord('a'))
    hexadental = '#' + str(r) + str(r2) + str(b) + str(b2) + str(c) + str(c2)
    return(hexadental)

print(hex(200, 255, 32))