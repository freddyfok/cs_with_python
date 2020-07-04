from node import Node
from stack import Stack


class TwoStackQueue:
    def __init__(self):
        self._old_on_top_stack = Stack()
        self._new_on_top_stack = Stack()

    def queue(self, value):
        new_node = Node(value)
        self._new_on_top_stack.add_item(new_node)

    def peek(self):
        self.check_empty()
        return self._old_on_top_stack.peek()

    def dequeue(self):
        self.check_empty()
        return self._old_on_top_stack.remove_item()

    def check_empty(self):
        if self._old_on_top_stack.is_empty():
            while not self._new_on_top_stack.is_empty():
                self._old_on_top_stack.add_item(self._new_on_top_stack.remove_item())
