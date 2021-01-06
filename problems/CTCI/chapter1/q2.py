"""
is a string permutation of another
"""


def is_permutation(str1: str, str2: str):
    if not len(str1) == len(str2):
        return False

    count_dict = {}
    for i in str1:
        if i not in count_dict:
            count_dict[i] = 0
        count_dict[i] += 1

    for i in str2:
        if i not in count_dict:
            return False
        count_dict[i] -= 1
        if count_dict[i] < 0:
            return False
    return True

if __name__ == "__main__":
    print(is_permutation("abcdef", "fedcba"))
    print(is_permutation("abcdef", "feecba"))
    print(is_permutation("abcdef", "feea"))
    print(is_permutation("", ""))

    str_ = "abc "
