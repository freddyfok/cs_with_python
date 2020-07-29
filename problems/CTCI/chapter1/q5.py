"""
one away
"""


def is_one_away(str_1, str_2):
    dif = len(str_1) - len(str_2)

    if dif == 0:
        return _replace_one(str_1, str_2)
    if dif == 1:
        return _insert_one(str_1, str_2)
    if dif == -1:
        return _insert_one(str_2, str_1)
    return False


def _replace_one(str_1, str_2):
    flag = False
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            if flag is False:
                flag = True
            else:
                return False
    return True


def _insert_one(str_1, str_2):
    i = 0
    j = 0

    while i < len(str_1) and j < len(str_2):
        if str_1[i] == str_2[j]:
            i += 1
            j += 1
        else:
            if j - i > 1:
                return False
            j += 1
    return True


if __name__ == "__main__":
    print(is_one_away("", ""))
    print(is_one_away("pale", "bale"))
    print(is_one_away("pale", "pae"))
    print(is_one_away("pale", "bail"))
