import unittest
from Lab11_2 import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_insert(self):
        tree = BinarySearchTree()
        tree.insert("apple", "a fruit")
        self.assertEqual(tree.root.term, "apple")
        self.assertEqual(tree.root.explanation, "a fruit")
        tree.insert("banana", "a fruit")
        self.assertEqual(tree.root.right.term, "banana")
        self.assertEqual(tree.root.right.explanation, "a fruit")
        tree.insert("cherry", "a fruit")

    def test_find(self):
        tree = BinarySearchTree()
        tree.insert("apple", "a fruit")
        tree.insert("banana", "a fruit")
        tree.insert("cherry", "a fruit")
        node = tree.find("banana")
        self.assertEqual(node.term, "banana")
        self.assertEqual(node.explanation, "a fruit")
        node = tree.find("orange")
        self.assertIsNone(node)

    def test_remove(self):
        tree = BinarySearchTree()
        tree.insert("apple", "a fruit")
        tree.insert("banana", "a fruit")
        tree.insert("cherry", "a fruit")
        tree.remove("banana")
        node = tree.find("banana")
        self.assertIsNone(node)

    def test_sorted_list(self):
        tree = BinarySearchTree()
        tree.insert("apple", "a fruit")
        tree.insert("banana", "a fruit")
        tree.insert("cherry", "a fruit")
        sorted_list = tree.sorted_list()
        self.assertEqual(sorted_list, [
            {"term": "apple", "explanation": "a fruit"},
            {"term": "banana", "explanation": "a fruit"},
            {"term": "cherry", "explanation": "a fruit"},
        ])

if __name__ == "__main__":
    unittest.main()