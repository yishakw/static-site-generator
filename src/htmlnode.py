class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    def props_to_html(self):
        if not self.props:
            return ""
        
        attr_str = ""
        for key, value in self.props.items():
            attr_str += f' {key}="{value}"'
        return attr_str
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"