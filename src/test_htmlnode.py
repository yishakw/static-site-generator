import unittest

from htmlnode import HTMLNode
class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("div", "Hello, world!", [], {"class": "test"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "test"})
    def test_eq(self):
        node1 = HTMLNode("div", "Hello, world!", [], {"class": "test"})
        node2 = HTMLNode("div", "Hello, world!", [], {"class": "test"})
        self.assertEqual(node1, node2)
    def test_neq(self):
        node1 = HTMLNode("div", "Hello, world!", [], {"class": "test"})
        node2 = HTMLNode("div", "Hello, world!", [], {"class": "test2"})
        self.assertNotEqual(node1, node2)
    def test_repr(self):
        node = HTMLNode("div", "Hello, world!", [], {"class": "test"})
        self.assertEqual(repr(node), "HTMLNode(div, Hello, world!, [], {'class': 'test'})")
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, world!", [], {"class": "test"})
        self.assertEqual(node.props_to_html(), ' class="test"')
