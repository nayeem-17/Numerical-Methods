import numpy as np
import matplotlib.pyplot as plt
import math


def error_calc(x_old, x_new):
    error = abs((x_new - x_old) / x_new)
    # print("error is ", error)
    return error


def bisection_method(
    x_points, y_points, lower_bound, upper_bound, rel_error=0.05, maxIteration=1000
):
    def func(b):
        xy = np.multiply(x_points, y_points)
        ebx = np.exp(np.multiply(x_points, b))
        e2bx = np.exp(np.multiply(x_points, 2 * b))
        return sum(np.multiply(xy, ebx)) - sum(np.multiply(y_points, ebx)) * sum(
            np.multiply(x_points, e2bx)
        ) / sum(e2bx)

    rel_error /= 100
    while True:
        avg = (lower_bound + upper_bound) / 2

        # print(
        #     "Lower bound is ",
        #     lower_bound,
        #     "upper bound is ",
        #     upper_bound,
        #     "avg is ",
        #     avg,
        # )
        if func(avg) == 0:
            return avg

        if func(lower_bound) > 0:
            # lb pos,ub neg, avg neg
            if func(avg) < 0:
                upper_bound = avg
            else:
                lower_bound = avg
        else:
            # lb neg, ub pos, avg pos
            if func(avg) > 0:
                upper_bound = avg
            else:
                lower_bound = avg
        if maxIteration == 0:
            return avg
        error = error_calc(avg, (lower_bound + upper_bound) / 2)
        if error <= rel_error:
            return (lower_bound + upper_bound) / 2
            break
        maxIteration -= 1


def solveOfExpModelByDT(x_points, y_points):
    sumOfXY = sum(np.multiply(x_points, y_points))
    sqSumOfX = sum(np.multiply(x_points, x_points))
    n = len(x_points)
    constants = dict()
    constants["a1"] = (n * sumOfXY - sum(x_points) * sum(y_points)) / (
        n * sqSumOfX - sum(x_points) * sum(x_points)
    )
    # constants["a0"] = (sqSumOfX * sum(y_points) - sum(x_points) * sumOfXY) / (
    #     n * sqSumOfX - sum(x_points) * sum(x_points)
    # )
    constants["a0"] = math.exp((sum(y_points) - constants["a1"] * sum(x_points)) / n)
    return constants


def solveOfExpModel(x_points, y_points):
    n = len(x_points)
    constants = dict()
    constants["a1"] = bisection_method(x_points, y_points, -10, 10)
    ebx = np.exp(np.multiply(x_points, constants["a1"]))
    e2bx = np.exp(np.multiply(x_points, 2 * constants["a1"]))
    constants["a0"] = sum(np.multiply(y_points, ebx)) / sum(e2bx)
    return constants


if __name__ == "__main__":
    x = []
    y = []
    n = int(input())
    for i in range(n):
        inputRowMat = input()
        inputRowMat = inputRowMat.split(" ")
        inputRowMat = [float(i) for i in inputRowMat]
        x.append(inputRowMat[0])
        y.append(inputRowMat[1])
    x_points = np.array(x)
    y_points = np.array(y)
    # for data transformation
    constants = solveOfExpModelByDT(x_points, np.log(y_points))
    # for normal solution
    # constants = solveOfExpModel(x_points, y_points)
    print(constants)
    plt.scatter(x_points, y_points)
    max_x_point = x_points[-1] + x_points[0]
    x_points = np.arange(0.001, max_x_point, 0.01)
    plt.plot(x_points, constants["a0"] * np.exp(x_points * constants["a1"]))
    plt.show()
