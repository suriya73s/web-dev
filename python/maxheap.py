# Priority Queue implementation in Python

# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        # Build the heap from the last non-leaf node
        for i in range((size // 2), -1, -1):
            heapify(array, len(array), i)

# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    if size == 0:
        print("Heap is empty")
        return

    for i in range(size):
        if array[i] == num:
            break
    else:
        print("Element not found")
        return

    # Swap with the last element and remove it
    array[i], array[size - 1] = array[size - 1], array[i]
    array.pop()

    # Rebuild the heap
    for i in range((len(array) // 2), -1, -1):
        heapify(array, len(array), i)

# Driver code
arr = []
insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
