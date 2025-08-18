import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Go to my website", {"href":"mywebsite.com"})
        self.assertEqual(node.to_html(), "<a>Go to my website</a>")


if __name__ == "__main__":
    unittest.main()
