"""
Given a list of arrays with duplicate elements, find the single number
"""


def find_single_number(array):
    x = 0
    for i in array:
        x ^= i
    return x


print(find_single_number([4,2,5,3,6,4,2,5,3]))
