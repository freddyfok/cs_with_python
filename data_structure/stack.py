"""
Stack, a abstract data type.
Stack is LIFO, meaning that the last item comes out first
Like stacking a plate. You don't take the plate from the bottom.
You take out the plate at the top first, which is the plate you put in last
Can be implemented with a simple python list
Or using Node to keep track of previous data

Used for Depth first search (DFS) because stack is good to keep track of recursion

time = o(n), bounded by how many operation
space = o(n), bounded by how many element in stacks
"""
from typing import Optional

from data_structure.node import Node


class StackList:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """check if stack is empty"""
        return self.stack == []

    def add_item(self, value):
        """add value to top of stack"""
        return self.stack.append(value)

    def peek(self):
        """value at top of the stack"""
        if not self.is_empty():
            return self.stack[-1]

    def remove_item(self):

        return self.stack.pop()


class Stack:
    def __init__(self):
        self._head: Optional[Node] = None

    def add_item(self, value: any):
        new_node = Node(value)
        new_node.next_node = self._head
        self._head = new_node

    def remove_item(self) -> Optional[any]:
        if self.is_empty():
            return None
        data = self._head.value
        self._head = self._head.next_node
        return data

    def peek(self) -> Optional[any]:
        if self._head is None:
            return None
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

