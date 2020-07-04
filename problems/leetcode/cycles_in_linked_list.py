# o(n) complexity, depends on how many nodes (n) in the list
from data_structure.node import Node


def check_linked_list_cycles(head: Node):
    if head is None:
        return False
    slow_node = head
    fast_node = head.next_node

    while slow_node is not fast_node:
        if fast_node is None or fast_node.next_node is None:
            return False
        slow_node = slow_node.next_node
        fast_node = fast_node.next_node.next_node
    return True


