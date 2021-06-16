# V =4 * pi *h^2 *r - 4 * pi * h^3/3 * (r- h/3)
V = 4
PI = 3.1416


def func(x_values):
    return 3 * PI * x_values ** 2 - PI * (x_values ** 3) / 3 - V


def error_calc(x_old, x_new):
    error = abs((x_new - x_old) / x_new)
    # print("error is ", error)
    return error


def bisection_method(lower_bound, upper_bound, rel_error=0.5, maxIteration=100):

    rel_error /= 100

    while True:
        avg = (lower_bound + upper_bound) / 2

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

        maxIteration -= 1


if __name__ == "__main__":

    print("The root is ", bisection_method(0.0, 6.0))