import re
import numpy as np
import matplotlib.pyplot as plt
import os


def GaussianElimination(A, B, d=False):
    dim = len(A)
    # forward elimination
    for i in range(dim - 1):
        for j in range(i, dim - 1):
            r = A[i][i] / A[j + 1][i]
            # in variable matrix
            B[j + 1] *= r
            B[j + 1] -= B[i]
            for k in range(dim):
                # in co-eff matrix
                A[j + 1][k] *= r
                A[j + 1][k] -= A[i][k]
            if d == True:
                print("The co-eff matrix is ...")
                for _ in A:
                    print(_)
                print("The variable matrix is ...")
                for _ in B:
                    print(_)
    # backward Substitution
    #  to make diag 1
    for i in range(dim):
        B[i] /= A[i][i]
        temp = A[i][i]
        for k in range(dim):
            A[i][k] /= temp
    for i in range(dim - 1):
        for k in range(i, dim - 1):
            B[dim - k - 2] -= B[dim - 1 - i] * A[dim - k - 2][dim - 1 - i]
            A[dim - k - 2][dim - 1 - i] = 0.0
    return B


def solveOfPolyModel(x_points, y_points, m):
    n = len(x_points)
    coeffArr = []
    varArr = []
    for i in range(m + 1):
        temp = []
        for j in range(m + 1):
            if i == 0 and j == 0:
                temp.append(n)
            else:
                temp.append(sum(np.power(x_points, j + i)))
        coeffArr.append(temp)

        if i == 0:
            varArr.append(sum(y_points))
        else:
            temp_x = np.power(x_points, i)
            sumOfnXY = sum(np.multiply(temp_x, y_points))
            varArr.append(sumOfnXY)
    # print(coeffArr)
    # print(varArr)
    result = GaussianElimination(coeffArr, varArr)
    return result


def getYValues(x_points, constants, m):
    y_points = np.zeros(len(x_points))
    for i in range(m + 1):
        y_points += np.multiply(np.power(x_points, i), constants[i])
    return y_points


if __name__ == "__main__":
    x = []
    y = []
    # n = int(input())
    # for i in range(n):
    #     inputRowMat = input()
    #     inputRowMat = inputRowMat.split(" ")
    #     inputRowMat = [float(i) for i in inputRowMat]
    #     x.append(inputRowMat[0])
    #     y.append(inputRowMat[1])
    # m = int(input())

    # input from file

    filepath = "input.txt"
    file = open(filepath)
    # inputs = file.readline()
    # inputs = inputs.split(" ")
    # n = int(inputs[0])
    # m = int(inputs[1])
    for line in file.readlines():
        # inputRowMat = file.readline()
        line = line.split(" ")
        line = [float(i) for i in line]
        x.append(line[0])
        y.append(line[1])
    file.close()

    n = len(x)
    print(n)

    x_points = np.array(x)
    y_points = np.array(y)
    plt.scatter(x_points, y_points, s=10)
    new_x_points = np.array(x_points)
    new_x_points.sort()
    max_x_point = abs(x_points[-1]) + abs(x_points[0])
    new_x_points = np.arange(new_x_points[0], max_x_point, 0.1)
    colors = ["black", "green", "red"]
    for i in range(3):
        constants = solveOfPolyModel(x_points, y_points, i + 1)
        print(constants)
        new_y_points = getYValues(new_x_points, constants, i + 1)
        plt.plot(new_x_points, new_y_points, color=colors[i])

    # constants = solveOfPolyModel(x_points, y_points, 2)
    # print(constants)
    # plt.plot(x_points, y_points, color=colors[0])

    plt.show()
