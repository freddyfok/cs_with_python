class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_dups(root: Node):
    if not root:
        return

    set_ = set()
    prev = None
    current = root

    while current:
        if current.value not in set_:
            set_.add(current.value)
            prev = current
        else:
            prev.next = current.next
        current = current.next


