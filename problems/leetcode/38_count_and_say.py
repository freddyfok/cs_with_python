def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    string = countAndSay(n - 1)
    count = 0
    tmp = string[0]
    ret_value = ""
    for i in range(len(string)):
        if string[i] == tmp:
            count += 1
        else:
            ret_value += str(count) + str(tmp)
            count = 1
            tmp = string[i]

    ret_value += str(count) + str(tmp)
    return ret_value
