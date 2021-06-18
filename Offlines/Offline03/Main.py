import pandas as pd
import numpy as np

u = 2000
m0 = 140000
g = 9.8
q = 2100


# def by_simpsons_rule1(n):
#     h = (30 - 8) / (2 * n)
#     result = 0
#     for i in range(2 * n + 1):
#         t = 8 + h * i
#         y = get_func(t)
#         if i == 0 or i == 2 * n:
#             result += y
#         elif i % 2 == 0:
#             result += 2 * y
#         else:
#             result += 4 * y
#         # print(y)
#     return result * h / 3


def error_calc(x_old, x_new):
    error = abs((x_new - x_old) / x_new)
    return error * 100


def by_simpsons_rule(n):
    start = 8
    end = 30
    h = (end - start) / (2 * n)
    result = 0
    for i in range(n):
        result += single_application_of_Simpsons_rule(start + i * 2 * h, h)
    return result


def single_application_of_Simpsons_rule(a, h):
    b = a + 2 * h
    return h * (get_func(a) + get_func(b) + 4 * get_func((a + b) / 2)) / 3


def by_trapezoid_rule(n):
    h = (30 - 8) / n
    result = 0
    for i in range(n + 1):
        t = 8 + h * i
        y = get_func(t)
        if i == 0 or i == n:
            result += y * 1.0 / 2
        else:
            result += y
    result = result * h
    return result


def get_func(t):
    return (u * np.log(m0 / (m0 - q * t))) - g * t


def print_T_error():
    x_val = []
    err = ["-"]
    index = np.arange(1, 6)
    x_old = by_trapezoid_rule(1)
    x_val.append(x_old)
    for i in range(2, 6):
        x_new = by_trapezoid_rule(i)
        x_val.append(x_new)
        err.append(error_calc(x_old=x_old, x_new=x_new))
        x_old = x_new
    table = {"Calculated values": x_val, "Error": err}
    df = pd.DataFrame(table)
    df.index = index
    print(df)
    print()


def print_S_error():
    x_val = []
    err = ["-"]
    index = np.arange(1, 6)
    x_old = by_simpsons_rule(1)
    x_val.append(x_old)
    for i in range(2, 6):
        x_new = by_simpsons_rule(i)
        x_val.append(x_new)
        err.append(error_calc(x_old=x_old, x_new=x_new))
        x_old = x_new
    table = {"Calculated values": x_val, "Error": err}
    df = pd.DataFrame(table)
    df.index = index
    print(df)
    print()


if __name__ == "__main__":

    N = int(input("Enter the value of N:"))
    print("By Trapezoid rule: ")
    print("The approximate value -> ", by_trapezoid_rule(N))
    print()
    print_T_error()
    print("By Simpson's 1/3 rule: ")
    print("The approximate value -> ", by_simpsons_rule(N))
    print()
    print_S_error()