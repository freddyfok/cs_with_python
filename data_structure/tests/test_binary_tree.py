import unittest

from data_structure.bst_recursive import BinarySearchTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinarySearchTree()

    def test_insert(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(4)

        self.assertEqual()
