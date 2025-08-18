import unittest

from textnode import TextNode, text_node_to_html_node, TextType


class Test_text_node_to_html_node(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK,  {"href":"/homepage"})
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node", {"href":"/homepage"})

    # def test_image(self):
    #     node = TextNode("", TextType.IMAGE, "/homepage")
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, "img")
    #     self.assertEqual(html_node.value, "")
    #     self.assertEqual(html_node.props, {"src": "/homepage","alt": ""})
    #
    def test_image(self):
         node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
         html_node = text_node_to_html_node(node)
         self.assertEqual(html_node.tag, "img")
         self.assertEqual(html_node.value, "")
         self.assertEqual(
             html_node.props,
             {"src": "https://www.boot.dev", "alt": "This is an image"},
         )



if __name__ == "__main__":
    unittest.main()
