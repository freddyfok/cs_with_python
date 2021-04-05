"""
Node class containing a value and pointer to next
"""
from typing import Optional


class Node:
    def __init__(self, value: any, next_: Optional["Node"] = None):
        self.value = value
        self.next_node = next_
