# python Program to Insert an element
# at a specific position in an Array


def insertElement(arr, n, x, pos):

    # shift elements to the right
    # which are on the right side of pos
    for i in range(n-1, pos-1, -1):
        arr[i + 1] = arr[i]

    arr[pos] = x
