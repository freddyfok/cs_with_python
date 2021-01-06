"""
Problem:
given a list of list holding min and max range (ie. [[12, 15], [1,5], [32, 34]])
return a random number within those ranges

approach 1:
you can build a list of all those numbers laid out, but it will take space

approach 2:
you know the range of those number, and therefore the supposed length of the list
"""
import random
from typing import List


def get_random(list_: List[List]):
    if not list_:
        return None

    length = 0
    for each_list in list_:
        length += each_list[-1] - each_list[0] + 1

    index = random.randrange(length)
    print(index)

    for each_list in list_:
        leng_tmp = each_list[-1] - each_list[0]
        if index > leng_tmp:
            index -= (leng_tmp + 1)
        else:
            return each_list[0] + index


print(get_random([[12, 15], [1,5], [32, 34]]))
