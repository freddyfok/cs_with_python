"""
string matching
brutal force method works, but expensive. o(mn) (ie o(n2))

Rabin-Karp Algorithm uses hashing and rolling hash to find patterns
ie. to find str of size 3 in text

first iteration:
total = h(str[0]) X h(str[1]) X h(str[2])
text total = h(text[0]) X h(text[1]) X h(text[2])

second iteration:
without redoing the text total, you just need to divide hast of text[0]
then multiply hash of text[3]
text total = text_total X h(text[3]) / h(text[0])
"""


def brute_force_method(string, target_string):
    n = len(string)
    m = len(target_string)

    counter = 0

    for char in range(m-n+1):
        found = True
        for i in range(m):
            if target_string[i] != string[char+i]:
                found = False
                break
        if found:
            counter += 1

    if counter == 0:
        print("No match")
    else:
        print(f"appeared {counter} times")


