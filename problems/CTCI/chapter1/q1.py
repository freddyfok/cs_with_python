"""
only unique characters in string
"""


def is_unique(string: str):
    set_ = set()
    for i in string:
        if i in set_:
            return False
        else:
            set_.add(i)
    return True


if __name__ == "__main__":
    print(is_unique("abcdef"))
    print(is_unique("abcddef"))
    print(is_unique(""))
