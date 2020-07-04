"""
[1,1,1,2,3]     k=1     answer = 3
[1,2,3,4,4,4]   k=3     answer = 1
[]              k=1     answer = 0
key info:
sorted
search

Linear search can be used, but it is o(n)
This problem can be solved o(log n) time, therefore use two binary searches

Find the first occurrence of k, find the last occurrence of K
first - last + 1 would be the answer
"""


def binary_search(arr, target, search_first):
    start = 0
    end = len(arr)-1
    result = -1
    while start <= end:
        mid = int(start + (end-start)/2)
        if target == arr[mid]:
            result = mid
            if search_first:
                end = mid - 1
            else:
                start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result


def total_occurrence(arr, target):
    first_value = binary_search(arr, target, True)
    second_value = binary_search(arr, target, False)
    return second_value - first_value +1


if __name__ == "__main__":
    array = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
    print(total_occurrence(array, 3))
