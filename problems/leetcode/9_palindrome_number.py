def isPalindrome(x) -> bool:
    if x < 0:
        return False

    old_number = x
    tmp = 0
    while x != 0:
        x, remainder = divmod(x, 10)
        tmp = tmp*10 + remainder

    if tmp == old_number:
        return True
    else:
        return False
