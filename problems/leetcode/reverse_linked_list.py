"""
To reverse a linked list
"""
from data_structure.linked_list import LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(node: Node):
    prev = None
    while node is not None:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp
    return prev  # new head


if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_1.next = node_2
    node_2.next = node_3
    new_head = reverse_linked_list(node_1)
    print(new_head.value, new_head.next.value, new_head.next.next.value)
