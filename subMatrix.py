import sys

# function returns a list of sums for each possible square sub-matrix of size k x k, given a square matrix
def subMatrixSums(matrix, k):

    # calculates dimension of matrix
    dimension = len(matrix)

    # doesn't allow for sub-matrix bigger than original matrix
    if k > dimension:
        print("K value not allowed")
        sys.exit()

    # calculates height of sumMatrix and creates empty sumMatrix
    tempHeight = dimension - k + 1
    sumMatrix = [[None] * dimension for i in range(tempHeight)]

    # calculates sum of all vertical strips of size k and stores sum value in sumMatrix
    for col in range(dimension):
        sum = 0

        for cell in range(tempHeight):
            sum += matrix[cell][col]
        sumMatrix[0][col] = sum

        for cell in range(1, tempHeight):
            sum += (matrix[cell + k - 1][col] - matrix[cell - 1][col])
            sumMatrix[cell][col] = sum

    # creates empty list to store sum of all sub-matrixes
    outMatrix = []

    # iterates over sumMatrix to calculate sum of all sub-matrixes and stores it in outMatrix
    for row in range(tempHeight):
        sum = 0

        for cell in range(k):
            sum += sumMatrix[row][cell]
        outMatrix.append(sum)

        for cell in range(1, tempHeight):
            sum += (sumMatrix[row][cell + k - 1] - sumMatrix[row][cell - 1])
            outMatrix.append(sum)

    return outMatrix


def subMatrixMin(matrix, k):
    return min(subMatrixSums(matrix, k))


def subMatrixMax(matrix, k):
    return max(subMatrixSums(matrix, k))


def main():
    testMatrix = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
    testMatrixTwo = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

    print(subMatrixSums(testMatrix, 3))
    print(subMatrixMin(testMatrix, 3))
    print(subMatrixMax(testMatrix, 3))
    print()
    print()
    print(subMatrixSums(testMatrixTwo, 2))
    print(subMatrixMin(testMatrixTwo, 2))
    print(subMatrixMax(testMatrixTwo, 2))


main()
