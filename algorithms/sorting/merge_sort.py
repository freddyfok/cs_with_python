"""
type of algo of merge sort
1) Divide and conquer
2) Recursive
3) Stable
4) Not in place

time: o(n logn)
space: o(n)
"""

def merge(left_array, right_array):
    tmp_array = []
    n = 0
    m = 0
    while n < len(left_array) and m < len(right_array):
        if left_array[n] >= right_array[m]:
            tmp_array.append(right_array[m])
            m += 1
        else:
            tmp_array.append(left_array[n])
            n += 1

    while n < len(left_array):
        tmp_array.append(left_array[n])
        n += 1

    while m < len(right_array):
        tmp_array.append(right_array[m])
        m += 1

    return tmp_array


def merge_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array

    list_left = [array[n] for n in range(int(len(array)/2))]
    list_right = [array[n] for n in range(int(len(array)/2), len(array))]

    list_left = merge_sort(list_left)
    list_right = merge_sort(list_right)

    return merge(list_left, list_right)


a = [1, 2, 3, 4, 5, 6, 7]
print(merge_sort(a))
