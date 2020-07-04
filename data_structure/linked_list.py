"""
Linked List

"""
from typing import Optional

from data_structure.node import Node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def prepend(self, value):
        # no need to check if self._head is none
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def delete_with_value(self, value):
        if self.head.value is None:
            return
        if value == self.head.value:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node is not None:
            if current_node.next_node.value == value:
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node

    def find_with_value(self):
        pass

    def insert_after_value(self):
        pass

