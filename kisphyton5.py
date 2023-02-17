import math


def main(y):
    ans = 0
    for i in range(len(y)):
        someVar1 = 63+(y[len(y)-math.ceil((i+1)/4)])**2
        someVar2 = 82*((y[len(y)-math.ceil((i+1)/4)])**3)
        ans += 57*((someVar1+someVar2)**6)
    return ans


print(main([-0.31, -0.12, 0.0, -0.45, 0.66, -0.67, -0.8, 0.19]))

