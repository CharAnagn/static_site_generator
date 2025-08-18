from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")

        if self.children is None:
            raise ValueError("invalid HTML: no children")


        child_string = ""
        for child in self.children:
            child_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"
