from data_structure.queue import Queue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_iterative(self, value):
        # done iteratively
        new_node = TreeNode(value)

        current_node = self.root
        trailing_node = None

        while current_node is not None:
            trailing_node = current_node
            if value <= current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if trailing_node is None:
            self.root = new_node
        elif value <= trailing_node.value:
            trailing_node.left = new_node
        else:
            trailing_node.right = new_node

    def insert_recursively(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if value <= root.value:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                self._insert(root.left, value)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                self._insert(root.right, value)

    def search_with_value_iteratively(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def search_with_value_recursively(self, value):
        if self.root is None:
            return False
        else:
            self._search(self.root, value)

    def _search(self, root, value):
        if value == root:
            return True
        elif value < root:
            self._search(root.left, value)
        else:
            self._search(root.right, value)

    def find_min_iteratively(self):
        if self.root is None:
            return
        current_node = self.root
        trailing_node = None
        while current_node is not None:
            trailing_node = current_node
            current_node = current_node.left
        return trailing_node.value

    def find_max_recursively(self, root):
        if root is None: return
        if root.right is None: return root.value
        return self.find_max_recursively(root.right)

    def find_height(self):
        # number of edges
        if self.root is None:
            return 0
        else:
            return self._find_height(self.root)

    def _find_height(self, root):
        if root is None:
            return -1
        else:
            left_height = self._find_height(root.left)
            right_height = self._find_height(root.right)
            return max(left_height, right_height) + 1

    def traversal_level_order(self):
        # o(n) for time
        # o(n) for space
        if self.root is None:
            return
        node_queue = Queue()
        node_queue.queue(self.root)
        value = []
        while not node_queue.is_empty():
            current_node = node_queue.de_queue()
            value.append(current_node.value)
            if current_node.left is not None:
                node_queue.queue(current_node.left)
            if current_node.right is not None:
                node_queue.queue(current_node.right)
        return value

    def traversal_pre_order(self, root, result=None):
        if result is None:
            result = []
        if root is None:
            return
        else:
            result.append(root.value)
            self.traversal_pre_order(root.left, result)
            self.traversal_pre_order(root.right, result)
        return result

    def traversal_in_order(self, root, result=None):
        if result is None:
            result = []
        if root is None:
            return
        else:
            self.traversal_in_order(root.left, result)
            result.append(root.value)
            self.traversal_in_order(root.right, result)

        return result

    def traversal_post_order(self):
        pass

    def is_BST(self, root):
        pass

    def _is_subtree_lesser(self):
        pass

