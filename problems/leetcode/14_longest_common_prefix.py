from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    if len(strs) == 1:
        return strs[0]

    prefix = strs[0]
    prefix_len = len(prefix)

    for s in strs[1:]:
        while prefix != s[0:prefix_len]:
            prefix = prefix[:-1]
            prefix_len = len(prefix)

            if prefix_len == 0:
                return ""

    return prefix


str[0] = flower
str[1] = flow
str[2] = flight
