import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_strong(self):
        node = LeafNode("strong", "Bold text")
        self.assertEqual(node.to_html(), "<strong>Bold text</strong>")

    def test_leaf_to_html_span_with_props(self):
        node = LeafNode("span", "Some text", props={"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Some text</span>')

    def test_leaf_to_html_img_with_props(self):
        node = LeafNode("img", "image.png", props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.png" alt="An image" />')

    def test_leaf_no_tag(self):
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_invalid_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)
