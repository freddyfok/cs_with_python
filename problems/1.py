"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


def find_equal(list_, k):  # simple way
    new_list = list_.copy()
    for element in list_:
        new_list = new_list.copy()
        del new_list[0]
        for number in new_list:
            if (element + number) == k:
                return True
    return False


def find_equal2(list_, k):  # easiest way
    old_elements = set()
    for element in list_:
        if (k-element) in old_elements:
            return True
        old_elements.add(element)
        return False


LIST = [15, 3, 10, 7]
K = 17

if __name__ == "__main__":
    #find_equal(LIST, K)
    find_equal2(LIST, K)
