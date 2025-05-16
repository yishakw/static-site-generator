from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self,tag, children,props=None):
        if not children:
            raise ValueError("ParentNode must have children")
        if not tag:
            raise ValueError("ParentNode must have a tag")
        super().__init__(tag, children, props)
        self.children = children
        self.tag = tag
        self.props = props or {}
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

   