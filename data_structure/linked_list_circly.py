from data_structure.node import Node


class CirclyLinkedList:
    def __init__(self):
        self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.tail = new_node
            self.tail.next_node = self.tail
            return

        head_node = self.tail.next_node
        self.tail.next_node = new_node
        new_node.next_node = head_node

    def append(self, value):
        self.prepend(value)
        self.tail = self.tail.next_node

    def delete_with_value(self, value):
        pass

    def find_with_value(self, value):
        pass

