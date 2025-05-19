import unittest

from htmlnode import HTMLNode
class TestHTMLnode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("div", "This is a div", props={"class": "container"})
        expected_repr = f"HTMLNode(tag=div, value=This is a div, children=None, props={{'class': 'container'}})"
        self.assertEqual(repr(node), expected_repr)
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' class="container"')
        node_no_props = HTMLNode("div", "This is a div")
        self.assertEqual(node_no_props.props_to_html(), "")
    

if __name__ == "__main__":
    unittest.main()