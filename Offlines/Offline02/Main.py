import numpy


def GaussianElimination(A, B, d=True):
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


if __name__ == "__main__":
    n = int(input())
    coeffmatrix = []
    variableMatrix = []
    for i in range(n):
        inputRowMat = input()
        inputRowMat = inputRowMat.split(" ")
        inputRowMat = [int(i) for i in inputRowMat]
        coeffmatrix.append(inputRowMat)
    input()
    for i in range(n):
        inputVal = float(input())
        variableMatrix.append(inputVal)
    answer = GaussianElimination(coeffmatrix, variableMatrix, d=False)

    print("The answer is ")
    for i in range(n):
        print("%0.4f" % (answer[i]))
