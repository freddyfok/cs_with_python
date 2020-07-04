#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy_head = ListNode(0)
    current = dummy_head

    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        carry, sum_ = divmod(l1_val+l2_val+carry, 10)

        current.next = ListNode(sum_)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry == 1:
        current.next = ListNode(1)

    return dummy_head.next


