
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
            continue

        splitted_text = node.text.split(delimiter)

        if len(splitted_text) % 2 == 0:
            raise Exception("invalid markdown, formatted section not closed")

        for index,part in enumerate(splitted_text):
            if index == 0 or index % 2 == 0:
                new_list.append(TextNode(part,TextType.TEXT))
            else:
                new_list.append(TextNode(part, text_type))
    return new_list
