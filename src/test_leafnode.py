import unittest

from htmlnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_l33t_speak(self):
        node = LeafNode("w", "H3ll0, w0rld!")
        self.assertEqual(node.to_html(), "<w>H3ll0, w0rld!</w>")
    def test_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()