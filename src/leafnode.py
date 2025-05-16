from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if not value:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, props)
        
        self.tag = tag
        self.value = value
        self.props = props or {}
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        if self.value:
            if self.tag == "img":
                return f"<{self.tag}{self.props_to_html()} />"
            elif self.tag == "a":
                return f"<{self.tag}{self.props_to_html()} href='{self.value}'>{self.value}</{self.tag}>"
            elif self.tag == "p":
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"          
            
            return f"LeafNode(<{self.tag} {self.props_to_html()}>{self.text}</{self.tag}>"
        else:
            return f"LeafNode<{self.tag}{self.props_to_html()}/>"

        