"""
if needle is in haystack, return the index of the first occurrence
"""

def str_str(haystack: str, needle: str):
    if not needle:
        return 0

    if len(needle) > len(haystack):
        return -1

    length = len(haystack.split(needle)[0])

    return length if length < len(haystack) else -1
