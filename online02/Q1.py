import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def calc_b(x, y):
    length = len(x)
    if length == 1:
        return y[0]
    dif = x[0] - x[length - 1]
    result = (calc_b(x[:-1], y[:-1]) - calc_b(x[1:], y[1:])) / dif
    # print(x)
    return result


def calc_value(x_point, y_point, x):
    n = len(x_point)
    b = []
    for i in range(n):
        temp = calc_b(x_point[::-1][i:], y_point[::-1][i:])
        b.append(temp)
    # print(x_point)

    product = 1
    b = b[::-1]
    result = b[0]
    for i in range(1, n):
        product = (x - x_point[i - 1]) * product
        result += b[i] * product
    return result


def interpolation():
    print("Input the number of points:")
    n = int(input())
    x_point = []
    y_point = []
    print("Input the points")
    for i in range(n):
        temp = input()
        temp = temp.split(" ")
        x_point.append(float(temp[0]))
        y_point.append(float(temp[1]))
    print("Enter the value of x")
    a = float(input())
    return calc_value(x_point, y_point, a)


def draw_graph(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    mass_x_points = [19, 22, 26, 28, 30]
    mass_y_points = [1203, 1245, 1378, 1315, 1475]
    result_5_point = calc_value(mass_x_points, mass_y_points, 25)
    result_4_point = calc_value(mass_x_points[:-1], mass_y_points[:-1], 25)
    approx_error = abs((result_5_point - result_4_point) / result_4_point) * 100
    print("For mass: ")
    print("The value of mass is ", result_5_point)
    print("The absolute approximate relative error ", approx_error)
    mass_x_points.append(25)
    mass_y_points.append(result_5_point)
    draw_graph(mass_x_points, mass_y_points)

    velocity_x_points = [19, 22, 26, 28, 30]
    velocity_y_points = [3000, 3500, 4000, 4500, 5000]
    result_5_point = calc_value(velocity_x_points, velocity_y_points, 25)
    result_4_point = calc_value(velocity_x_points[:-1], velocity_y_points[:-1], 25)
    approx_error = abs((result_5_point - result_4_point) / result_4_point) * 100
    print("For velocity: ")
    print("The value of velocity is ", result_5_point)
    print("The absolute approximate relative error ", approx_error)
    velocity_x_points.append(25)
    velocity_y_points.append(result_5_point)
    draw_graph(velocity_x_points, velocity_y_points)
