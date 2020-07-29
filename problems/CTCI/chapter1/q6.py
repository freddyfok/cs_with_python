"""
string compression
"""

def string_compression(string):
    if not string:
        return False

    length = len(string)
    list_ = [None]*length
    list_index = 0
    string_index = 0
    count = 1

    while string_index < length:
        if not list_[list_index]:
            list_[list_index] = string[string_index]
            string_index += 1
            continue
        if string[string_index] == list_[list_index]:
            string_index += 1
            count += 1
        else:
            list_index += 1
            list_[list_index] = str(count)
            count = 0
            list_index += 1

