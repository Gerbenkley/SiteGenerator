import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        test_html1 = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        test_html2 = {
            "target": "_blank",
            "href": "https://www.google.com",
        }

        node1 = HTMLNode(props=test_html1)
        node2 = HTMLNode(props="")
        node3 = HTMLNode()
        node4 = HTMLNode(props=test_html2)
        targetstring1 = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(node1.props_to_html(), targetstring1)
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), "")
        self.assertEqual(node4.props_to_html(), targetstring1)
        print("htmlnodes asserted")



        leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leafnode2 = LeafNode("p", "This is a paragraph of text.")

        self.assertEqual(leafnode.to_html(), '<a href="https://www.google.com">Click me!</a>')
        self.assertEqual(leafnode2.to_html(), '<p>This is a paragraph of text.</p>')


if __name__ == "__main__":
    unittest.main()