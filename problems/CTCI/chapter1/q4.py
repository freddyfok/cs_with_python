"""
given a string, check if the permutation of the string is a palindrome as well
"""


def is_perm_palindrome(string: str) -> bool:
    set_ = set()
    for i in string:
        if i not in set_:
            set_.add(i)
        else:
            set_.remove(i)

    if len(set_) > 1:
        return False
    return True

if __name__ == "__main__":
    print(is_perm_palindrome("code"))
    print(is_perm_palindrome("aab"))
    print(is_perm_palindrome("carerac"))
