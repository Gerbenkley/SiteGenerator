import unittest

from htmlnode import HTMLNode

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
        targetstring1 = ' href="https://www.google.com" target="_blank"'
        node2 = HTMLNode(props="")
        node3 = HTMLNode()
        node4 = HTMLNode(props=test_html2)

        self.assertEqual(node1.props_to_html(), targetstring1)
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), "")
        self.assertEqual(node4.props_to_html(), targetstring1)
        print("htmlnodes asserted")



if __name__ == "__main__":
    unittest.main()