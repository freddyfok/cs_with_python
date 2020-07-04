def reverse(x: int) -> int:
    min_int = -2 ** 31
    max_int = 2 ** 31 - 1
    neg_flag = False

    if x < 0:
        neg_flag = True
        x = 0 - x

    tmp = 0
    while x != 0:
        x, remainder = divmod(x, 10)
        if tmp == int(min_int / 10) and remainder > 8 or tmp > int(min_int / 10): return 0
        if tmp == int(max_int / 10) and remainder > 7 or tmp > int(max_int / 10): return 0
        tmp = tmp * 10 + remainder

    if neg_flag: tmp = 0 - tmp

    return tmp
