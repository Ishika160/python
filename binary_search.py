def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] < x:
            left = mid + 1
        
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [10, 20, 30, 40, 50, 60]
x = 30
result = binary_search(arr, x)

if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the array.")
