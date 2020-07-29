"""
Return true if left of the center is
"""


from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode) -> bool:
    q = Queue()
    q.put(root)
    q.put(root)

    while not q.empty():
        left = q.get()
        right = q.get()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.value != right.value:
            return False

        q.put(left.left)
        q.put(right.right)
        q.put(left.right)
        q.put(right.left)
    return True
