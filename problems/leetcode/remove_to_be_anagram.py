"""
given two strings, how many characters minimum to remove from both
strings to get an anagram
"""


def remove_char_count(str1, str2):
    number_of_char = 26
    str1_count = [0]*number_of_char
    str2_count = [0]*number_of_char

    for i in range(len(str1)):
        str1_count[ord(str1[i]) - ord("a")] += 1

    for i in range(len(str2)):
        str2_count[ord(str2[i]) - ord("a")] += 1

    count = 0
    for i in range(number_of_char):
        count += abs(str1_count[i] - str2_count[i])

    return count
