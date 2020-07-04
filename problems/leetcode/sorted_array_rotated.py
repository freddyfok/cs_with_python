"""
problem statement:
find how many times the array rotated
this function only works when the array does not have duplicates

[6,7,1,2,3,4,5] return 2
"""


def find_rotate_number(array):
    start = 0
    n = len(array)
    end = n-1

    while start <= end:
        if array[start] < array[end]:  # case 1
            # if start is smaller than end, you got the sorted array
            # therefore you just return start
            # this works when the loops comes around because
            # it always starts next of last mid
            return start

        mid = start + (end - start)//2
        next_ = (mid + 1) % n
        prev = (mid + n - 1) % n
        if array[mid] < array[next_] and array[mid] < array[prev]:  # case 2
            # when you found the pivot point, just return mid
            return mid
        elif array[mid] <= array[end]:  # case 3
            # when mid element is smaller than end
            # the pivot won't be here, need to search left half
            end = mid - 1
        elif array[mid] >= array[start]:  # case 4
            # when mid element is greater than start
            # this means this section of the array is sorted
            # pivot doesn't exist here
            start = mid + 1
    return -1


if __name__ == "__main__":
    arr = [7,8,9,1,2,3,4,5]
    print(find_rotate_number(arr))
