import math
from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value, root=None):
        # done recursively
        if self.root is None:
            self.root = TreeNode(value)
            return
        if root is None:
            root = self.root
        if value <= root.value:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self.insert(value, root.left)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self.insert(value, root.right)

    def search(self, value):
        # done recursively
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None:
            return False
        if value == root.value:
            return True
        elif value < root.value:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)

    def get_height(self):
        # recursively get the number of edges
        if self.root is None:
            return 0
        return self._get_height(self.root)

    def _get_height(self, root):
        if root is None:
            return -1
        left = self._get_height(root.left)
        right = self._get_height(root.right)
        return max(left, right) + 1

    def find_min(self):
        # recursively
        if self.root is None:
            return
        else:
            return self._find_min(self.root)

    def _find_min(self, root):
        if root.left is None:
            return root.value
        else:
            return self._find_min(root.left)

    def is_BST(self):
        return self._is_BST(self.root, -math.inf, math.inf)

    def _is_BST(self, root, lower_bound, upper_bound):
        if root is None:
            return True
        if lower_bound < root < upper_bound\
                and self._is_BST(root.left, lower_bound, root.value)\
                and self._is_BST(root.right, root.value, upper_bound):
            return True
        return False

    def level_order_traversal(self) -> List[int]:
        ordered_list = []
        if self.root is None:
            return ordered_list
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)
            ordered_list.append(node.value)
        return ordered_list

    def traversal_in_order(self):
        list_ = []
        if self.root is None:
            return list_
        return self._in_order(self.root, list_)

    def _in_order(self, root, list_):
        if root is None:
            return
        self._in_order(root.left, list_)
        list_.append(root.value)
        self._in_order(root.right, list_)
        return list_

    def delete(self, value):
        self._delete(self.root, value)

    def _delete(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:  # value is found
            # case 1 and 2, where there is no child/one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.value = self._find_min(root.right)
                root.right = self._delete(root.right, root.value)
        return root


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)

    print(tree.search(5))
    print(tree.search(3))
    print(tree.search(7))

    print(tree.get_height())
    print(tree.find_min())

    print(tree.traversal_in_order())

    tree.delete(3)
    print(tree.traversal_in_order())


