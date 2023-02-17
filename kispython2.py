import math


def main(x):
    if x < 53:
        return 66*(x**6)
    if x < 126:
        return 98*((x**2+x)**4) - 57*(x**6)
    if x < 140:
        a = x**2 - 65*(math.floor(x)**3)
        b = (((math.log(x**3 + x**2 + 72*x, 10))**7)/53)
        return a - b
    else:
        return 73*((1+97*x+x**2)**4) + (84*(x**3))**6


print(main(79))
print(main(53))
print(main(186))
print(main(103))
print(main(49))

