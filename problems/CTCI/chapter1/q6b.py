def string_compression(string):
    if not string:
        return string

    current = string[0]
    count = 1
    array_ = []

    for i in range(1, len(string)):
        if string[i] == current:
            count += 1
        else:
            array_.append(current)
            array_.append(str(count))
            current = string[i]
            count = 1
    array_.append(current)
    array_.append(str(count))

    if len(string) <= len(array_):
        return string
    else:
        return "".join(array_)

if __name__ == "__main__":
    print(string_compression("a"))
