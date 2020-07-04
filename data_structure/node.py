"""
Node class containing a value and pointer to next
"""
from typing import Optional


class Node:
    def __init__(self, value: any):
        self.value: any = value
        self.next_node: Optional[Node] = None
