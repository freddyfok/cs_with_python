"""
Bubble sort is an O(n**2) sort.
For the number of elements in an array,
you bubble the largest number to the end.
5,4,3,2,1
4,5,3,2,1
4,3,5,2,1
...
"""


def bubble_sort(array):
    for j in range(1, len(array)):  # for every number in the array
        for i in range(len(array)-j):  # length of the array -j because array size shrink per j pass
            if array[i] > array[i+1]:
                array[i], array[i + 1] = array[i+1], array[i]
    return array


#testing
arr = [5,2,4,6,7,9,2,3,5,1]
print(bubble_sort(arr))
