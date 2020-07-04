class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    current = dummy_head
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy_head.next
