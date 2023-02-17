import math


def main(b, n, a, x):
    sb = 0
    for c in range(1, b+1):
        sb += 58*(math.exp(c)**2) + 78
    si = 0
    for c in range(1, a+1):
        sk = 0
        for k in range(1, b+1):
            sj = 1
            for i in range(1, n+1):
                part1 = (math.tan(x**2 + 1)**2) + 13*(i**6)
                sj *= part1 + (55 + k**2 + 35*(c**3))**3
            sk += sj
        si += sk
    return sb - si


print(main(8, 6, 6, 0.53))


