import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode,TextType

class Test_split_nodes_delimiter(unittest.TestCase):

    def test_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
             TextNode("This is text with a ", TextType.TEXT),
             TextNode("code block", TextType.CODE),
             TextNode(" word", TextType.TEXT),
         ])

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
             TextNode("This is text with a ", TextType.TEXT),
             TextNode("bold", TextType.BOLD),
             TextNode(" word", TextType.TEXT),
         ])


    def test_italic(self):
        node = TextNode("This is text with a __italic__ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.ITALIC)
        self.assertEqual(new_nodes, [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ])



if __name__ == "__main__":
    unittest.main()
