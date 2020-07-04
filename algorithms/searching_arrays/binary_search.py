"""
o(log n) search

The algorithm iteratively is as follows
the condition is you take the first and last element
find the mid point element and compare with target
if target is greater, go right, else go left

The algorithm for recursively is as follows
you need to know the start and ending element
compare target to middle element
adjust the starting and ending element
call the function again
"""


def binary_search_iterative(array, target, length):
    start = 0
    end = length - 1

    while start <= end:
        mid = start + end / 2  # start + ((end - start) / 2) for no overflow
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search_recursion(array, low, high, target):
    if low > high:
        return -1
    mid = low + (high - low) / 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_search_recursion(array, low, mid-1, target)
    else:
        binary_search_recursion(array, mid+1, high, target)
