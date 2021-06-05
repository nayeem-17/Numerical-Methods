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


if __name__ == "__main__":
    print("The value of y is ", interpolation())
    mass_x_points = []
