def linear_search(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50, 60]
x = 30
result = linear_search(arr, x)

if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the array.")
