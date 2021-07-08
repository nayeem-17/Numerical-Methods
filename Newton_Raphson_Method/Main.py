# TODO
#  Need to implement
import numpy as np
from numpy.core.numeric import NaN
import matplotlib.pyplot as plt


def getFunction(x):
    return x * x * x - 0.165 * x * x + 3.993 / 10000


def DofFunction(x):
    return 3 * x * x - 2 * 0.165 * x


def getError(x_new, x_old):
    return abs(1 - x_old / x_new)


def NewTonRaphspnMethod(x, e=0.05):
    e /= 100
    dofF = DofFunction(x)
    y = getFunction(x)
    if dofF == 0:
        print("Can't divide by 0")
        return NaN
    xNext = x - y / dofF
    if getFunction(xNext) == 0:
        return xNext
    error = getError(xNext, x)
    # print(error)
    if error <= e:
        return xNext
    else:
        return NewTonRaphspnMethod(xNext, e * 100)


if __name__ == "__main__":
    result = NewTonRaphspnMethod(0.05)
    if result == NaN:
        exit(1)
    max_x_point = 0.6
    print(result)
    x_points = np.arange(-0.5, max_x_point, 0.01)
    plt.plot(x_points, getFunction(x_points))
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    plt.scatter([result], [getFunction(result)])
    plt.grid()
    plt.legend()
    plt.show()