"""
Assumption: the string passed into the function an always valid roman number
Therefore,
"""


def roman_to_int(string) -> int:
    num_dict = {
        "M": 1000
        , "D": 500
        , "C": 100
        , "L": 50
        , "X": 10
        , "V": 5
        , "I": 1
    }

    special_set = ("C", "X", "I")
    sum_ = num_dict[string[0]]

    for i in range(1, len(string)):
        sum_ += num_dict[string[i]]

        prev = string[i-1]
        if num_dict[prev] < num_dict[string[i]] and prev in special_set:
            sum_ -= num_dict[prev]*2
    return sum_


print(roman_to_int("III"))
print(roman_to_int("MCMXCIV"))