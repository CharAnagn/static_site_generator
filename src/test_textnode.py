import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print(node, node2)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        print(node, node2)
        self.assertNotEqual(node, node2)

    def test_ne_text(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node random", TextType.BOLD, "https://www.boot.dev")
        print(node, node2)
        self.assertNotEqual(node, node2)

    def test_ne_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        print(node, node2)
        self.assertNotEqual(node, node2)




if __name__ == "__main__":
    unittest.main()
