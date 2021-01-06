"""
partition
"""


class Node:
    def __init__(self, data, next_ = None):
        self.data = data
        self.next = next_


def partition(node, target):
    if not node:
        return node

    current = node
    greater_list = None
    greater_list_tail = None
    smaller_list = None
    smaller_list_tail = None

    while current:
        tmp = current
        current = current.next
        tmp.next = None

        if tmp.data >= target:
            greater_list, greater_list_tail = add_to_list(greater_list, greater_list_tail, tmp)
        else:
            smaller_list, smaller_list_tail = add_to_list(smaller_list, smaller_list_tail, tmp)

    smaller_list_tail.next = greater_list
    return smaller_list


def add_to_list(head_node, tail_node, insert_node):
    if not head_node:
        head_node = insert_node
        tail_node = head_node
    else:
        tail_node.next = insert_node
        tail_node = tail_node.next

    return head_node, tail_node


if __name__ == "__main__":
    one = Node(1, None)
    two = Node(2, one)
    ten = Node(10, two)
    five1 = Node(4, ten)
    eight = Node(9, five1)
    five2 = Node(5,eight)
    three = Node(3, five2)

    partition(three, 5)
