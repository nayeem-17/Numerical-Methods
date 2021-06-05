def calcL(x_points, a, i):
    result = 1
    length = len(x_points)
    for j in range(length):
        if i != j:
            result *= (a - x_points[j]) / (x_points[i] - x_points[j])
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
    result = 0
    for i in range(n):
        result += calcL(x_point, a, i) * y_point[i]
    return result


if __name__ == "__main__":
    print(interpolation())
