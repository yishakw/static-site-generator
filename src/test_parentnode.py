import unittest
from parentnode import ParentNode
from leafnode import LeafNode
class TestParentNode(unittest.TestCase):
    def test_parent_node_init(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.tag, "div")
        self.assertEqual(parent_node.children, [child_node])
        self.assertEqual(parent_node.props, {})
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "test"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="test"><span>child</span></div>',
        )