"""
you want to write a ransom note
to avoid detection, you want to cut letters from magazine
1) no punctuation
2) case sensitive
are there enough words to build the ransom notes from magazine

method 1: brute force o(n*m)
you go through the note, cross out the word in the magazine when it matches
doesnt work if you have 5 of 1 string in note, and only 1 in magazine

method 2:
hash the magazine
hash the note
"""
from typing import List


def ransom_note(magazine: List[str], note: List[str]) -> bool:
    if len(note) > len(magazine) or not magazine or not note:
        return False

    magazine_dict = dict()
    for i in magazine:
        if i not in magazine_dict:
            magazine_dict[i] = 0
        magazine_dict[i] += 1

    for i in note:
        if i not in magazine_dict:
            return False
        magazine_dict[i] -= 1
        if magazine_dict[i] == 0:
            del magazine_dict[i]

    return True

str_1 = "some stupid people are stupid"
str_2 = "some stupid as"
str_1 = str_1.split(" ")
str_2 = str_2.split(" ")

print(ransom_note(str_1, str_2))
