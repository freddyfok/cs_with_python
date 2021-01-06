class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


def return_kth_to_last(root, k):
    if not root:
        return root

    count = 0
    current = root
    while count < k:
        if not current.next:
            return None
        current = current.next
        count += 1

    kth = root
    while current.next:
        kth = kth.next
        current = current.next

    return kth.value


if __name__ == "__main__":
    first = Node(1)
    second = Node(2, first)
    third = Node(3, second)
    fourth = Node(4, third)
    fifth = Node(5, fourth)
    sixth = Node(6, fifth)

    print(return_kth_to_last(sixth, 5))
