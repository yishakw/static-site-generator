from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if not value:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value,None,  props)
        
        self.tag = tag
        self.value = value
        self.props = props or {}
    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        