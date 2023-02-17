import math


def main(n):
    if n == 0:
        return 0.18
    else:
        part = 4 * (math.log(main(n - 1) ** 2))**2
        return part + (math.log(main(n - 1), 10)) ** 3


print(main(1))
