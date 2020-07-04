"""
problem statement:
count the number of occurence in an array
because linear search is o(n)
you can use binary search instead
use binary search to find the first element
then use binary search to find the last element
then you take the difference
"""


def occurrence_using_binary_search(arr, target):
    first_element = search(arr, target, True)
    if first_element == -1:
        return -1
    second_element = search(arr, target, False)
    return second_element - first_element + 1

    
def search(arr, target, search_first):
    low = 0
    high = len(arr)-1
    result = -1

    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == target:
            result = mid
            if search_first:
                high = mid - 1  # finds the minimum
            else:
                low = mid + 1  # finds the maximum element
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


if __name__ == "__main__":
    array = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
    print(occurrence_using_binary_search(array, 6))

