import numpy as np
import matplotlib.pyplot as plt


def solveByLinearRegression(x_points, y_points):
    sumOfXY = sum(np.multiply(x_points, y_points))
    sqSumOfX = sum(np.multiply(x_points, x_points))
    n = len(x_points)
    constants = dict()
    constants["b1"] = (n * sumOfXY - sum(x_points) * sum(y_points)) / (
        n * sqSumOfX - sum(x_points) * sum(x_points)
    )
    # constants["b0"] = (sqSumOfX * sum(y_points) - sum(x_points) * sumOfXY) / (
    #     n * sqSumOfX - sum(x_points) * sum(x_points)
    # )
    constants["b0"] = (sum(y_points) - constants["b1"] * sum(x_points)) / n
    return constants


def solveByLinearRegressionSC(x_points, y_points):
    sumOfXY = sum(np.multiply(x_points, y_points))
    sqSumOfX = sum(np.multiply(x_points, x_points))
    return sumOfXY / sqSumOfX


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
    constants = solveByLinearRegression(x_points, y_points)
    plt.scatter(x_points, y_points)
    x_points = np.append(x_points, [x_points[-1] + x_points[0]])
    plt.plot(x_points, constants["b0"] + x_points * constants["b1"])
    plt.show()
