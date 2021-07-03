import numpy as np
import matplotlib.pyplot as plt
import math


def error_calc(x_old, x_new):
    error = abs((x_new - x_old) / x_new)
    # print("error is ", error)
    return error


def bisection_method(
    x_points, y_points, lower_bound, upper_bound, rel_error=0.005, maxIteration=1000
):
    def func(b):
        xy = np.multiply(x_points, y_points)
        ex = np.exp(x_points)
        e2x = np.multiply(ex, ex)
        a = (
            sum(np.multiply(x_points, y_points)) - b * sum(np.multiply(x_points, ex))
        ) / sum(np.multiply(x_points, x_points))
        return (
            b * sum(e2x)
            + a * sum(np.multiply(x_points, ex))
            - sum(np.multiply(y_points, ex))
        )

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


def solveOfExpModel(x_points, y_points):
    n = len(x_points)
    constants = dict()
    constants["b"] = bisection_method(x_points, y_points, -10, 10)
    ex = np.exp(x_points)
    e2x = np.multiply(ex, ex)
    constants["a"] = (
        sum(np.multiply(y_points, x_points))
        - constants["b"] * sum(np.multiply(x_points, ex))
    ) / sum(np.multiply(x_points, x_points))
    return constants


if __name__ == "__main__":
    x = []
    y = []
    filepath = "data.txt"
    file = open(filepath)
    for line in file.readlines():
        line = line.split(" ")
        line = [float(i) for i in line]
        x.append(line[0])
        y.append(line[1])
    file.close()

    n = len(x)
    x_points = np.array(x)
    y_points = np.array(y)
    plt.scatter(x_points, y_points, s=10)
    constants = solveOfExpModel(x_points, y_points)
    # for normal solution
    # constants = solveOfExpModel(x_points, y_points)
    print(constants)
    plt.scatter(x_points, y_points)
    max_x_point = x_points[-1] + x_points[0]
    x_points = np.arange(0, 2, 0.01)
    calculated_y_values = np.multiply(constants["a"], x_points) + np.multiply(
        constants["b"], np.exp(x_points)
    )
    print(len(y_points))
    plt.plot(x_points, calculated_y_values, color="black")
    plt.show()