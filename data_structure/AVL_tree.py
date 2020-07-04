"""
Four steps approach
1) insert/delete like normal
2) update the tree height
3) find if the height is balanced
4) fix the balancing by rotating

all are done recursively
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    value: any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
    height: int = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, root, value):
        # insert like a normal BST
        if root is None:
            return TreeNode(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        # update the height of the tree at the current node
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        dif = left_height - right_height
        root.height = max(left_height, right_height) + 1

        # check if the tree is balanced
        if abs(dif) <= 1:
            return root

        if dif > 1 and value < root.left.value:
            return self.left_rotate(root)

    @staticmethod
    def get_height(root):
        if root is None:
            return -1
        return root.height

    def left_rotate(self, root):
        # rotate
        new_root = root.right
        tree_to_move = new_root.left

        new_root.left = root
        root.left = tree_to_move

        # after you rotate, update the heights
        root.height = 1 + max(
            self.get_height(root.left)
            , self.get_height(root.right)
        )

        new_root.height = 1 + max(
            root.height
            , self.get_height(new_root.right)
        )

        return new_root






