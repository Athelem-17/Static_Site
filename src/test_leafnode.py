import unittest
from htmlnode import LeafNode  # Replace `your_module` with the file name where LeafNode is defined

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Raw text only.")
        self.assertEqual(node.to_html(), "Raw text only.")

    def test_leaf_no_value(self):
        node = LeafNode("p")  # No value provided, so this is still valid.
        with self.assertRaises(ValueError):
            node.to_html()  # This should raise the ValueError as per your implementation.