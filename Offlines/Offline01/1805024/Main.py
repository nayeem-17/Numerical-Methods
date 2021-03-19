# Id - 1805024
# Course - CSE218S
# Date- 19 March, 2021

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# K=x/(1-x) *√(2pt/(2+x))

pt = 3
k = 0.05


def func(x_values):
    return (x_values / (1 - x_values)) * (2 * pt / (2 + x_values)) ** 0.5 - k


def error_calc(x_old, x_new):
    error = abs((x_new - x_old) / x_new)
    # print("error is ", error)
    return error


def draw_graph():

    x_values = np.arange(-1.001, 5, 0.01)
    y_values = func(x_values)
    y_values[:-1][np.diff(y_values) < 0] = np.nan

    plt.plot(x_values, y_values)
    plt.grid()
    plt.show()


def bisection_method(lower_bound, upper_bound, rel_error, maxIteration):
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


def show_table(lower_bound, upper_bound, maxIteration):
    # Modify the above method (as a second function/program) to output a table showing the
    # absolute relative approx. error after each iteration of the bisection method for up
    # to 20 iterations
    x_val = []
    err = ["-"]
    for _ in range(maxIteration):
        avg = (lower_bound + upper_bound) / 2
        x_val.append(avg)
        if func(avg) == 0:
            break

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
        maxIteration -= 1

        if maxIteration == 0:
            break
        error = error_calc(avg, (lower_bound + upper_bound) / 2)
        err.append(error * 100)

    table = {"values": x_val, "error": err}
    df = pd.DataFrame(table)
    df.index = np.arange(1, 21)
    # displaying the DataFrame
    print(df)


if __name__ == "__main__":
    draw_graph()
    print("The root is ", bisection_method(-1, 0.9, 0.5, 1000))
    show_table(-0.5, 0.5, 20)
