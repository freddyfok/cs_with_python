"""
Testing node class
"""
import unittest
from data_structure.node import Node


class TestNode(unittest.TestCase):
    node_int = Node(5)
    node_str = Node("yo")
    node_node = Node(node_int)

    def test_node(self):
        self.assertEqual(5, self.node_int.value)
        self.assertEqual(None, self.node_int.next_node)

        self.node_int.next_node = self.node_str
        self.assertEqual(self.node_str, self.node_int.next_node)
        self.assertEqual("yo", self.node_str.value)

        self.assertEqual(self.node_int, self.node_node.value)


if __name__ == "__main__":
    unittest.main()
