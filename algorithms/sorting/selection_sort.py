"""
selection sort
basically, you linear search for the smallest
then put it in the next available index
"""


def selection_sort(arr):
    for i in range(len(arr)):
        min_ = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_:
                min_ = arr[j]
