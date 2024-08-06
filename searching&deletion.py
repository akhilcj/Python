from array import array


# Function to search for a key in the array
def findElement(arr, n, key):
    for i in range(n):
        # Return the index if key is found
        if arr[i] == key:
            return i
    # Return -1 if key is not found
    return -1


# Function to delete an element from the array
def deleteElement(arr, n, key):
    # Find position of element to be deleted
    pos = findElement(arr, n, key)

    if pos == -1:
        print("Element not found")
        return n

    # Deleting element
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]

    return n - 1

