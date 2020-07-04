"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""


def product_of_all(list_: list):
    product_list = []
    for number in range(len(list_)):
        product = 1
        for num in range(len(list_)):
            if num == number:
                continue
            product = product * num
        product_list.append(product)
    return product_list


if __name__ == "__main__":
    some_list = [1, 2, 3, 4, 5]
    print(product_of_all(some_list))


