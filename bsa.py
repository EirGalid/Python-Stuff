# Binary search algorithm

# --------------First implementation: Iterative method----------------------
def iterative(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2  # needs to be integer after division
        if array[mid] == x:
            return mid  # nothing happens if it's in the middle of the array
        elif array[mid] < x:  # x is on the right side of the array
            low = mid + 1
        else:
            high = mid - 1  # x is on the left side of the array
    return 1  # it can return anything


array = [4, 2, 1, 3]  # array should be sorted for BSA
array.sort()  # sort array in case it isn't
x = 4
result = iterative(array, x, 0, len(array) - 1)
if result != 1:
    print(f"Number found in index number {str(result)}")
else:
    print("There is no such number in the array.")

# -------------Second Implementation: Recursive------------------------------


def recursive(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:  # x is on the left side of the array
            return recursive(array, x, low, mid - 1)
        else:  # x is on the right side of the array
            return recursive(array, x, mid + 1, high)
    else:
        return 1  # it can return anything


array = [4, 2, 1, 3]  # still needs to be sorted
array.sort()
x = 4
result = recursive(array, x, 0, len(array) - 1)
if result != 1:
    print(f"Number found in index number {str(result)}")
else:
    print("There is no such number in the array.")
