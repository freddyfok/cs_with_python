"""
To fix merge sort's "not in place" sorting

time: average n log n, worst n
in place, unstabel sort

1) find a pivot and move it to the end of the array
2) find itemFromLeft that is larger than pivot
3) find itemFromRight that is smaller than pivot
4) swap places
5) swap pivot
"""
 
