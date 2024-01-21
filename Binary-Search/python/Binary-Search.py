def binary_search(arr, item):
    right = len(arr) - 1
    left = 0
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == item:
            return middle
        elif arr[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
    if left > right:
        return -1


# must have sorting array
numbers_arr = [10, 20, 30, 40, 50, 60]
target = 40
index = binary_search(numbers_arr, target)
if index == -1:
    print("item not found")
else:
    print("Item found at index", index)
