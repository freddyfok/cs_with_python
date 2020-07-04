from typing import Optional


class SpecialNode:
    def __init__(self, value: any):
        self.value = value
        self.next_node: Optional[SpecialNode] = None
        self.previous: Optional[SpecialNode] = None


class LinkedListCircleDoubly:
    def __init__(self):
        self._tail = None

    def prepend(self, value):
        new_node = SpecialNode(value)
        if self._tail is None:
            self._tail = new_node
            self._tail.next_node = self._tail
            self._tail.previous = self._tail
            return

        new_node.previous = self._tail
        new_node.next_node = self._tail.next_node

        if self._tail.previous is self._tail:
            self._tail.previous = new_node
        else:
            self._tail.next_node.previous = new_node
        self._tail.next_node = new_node

    def append(self, value):
        self.prepend(value)
        self._tail = self._tail.next_node
