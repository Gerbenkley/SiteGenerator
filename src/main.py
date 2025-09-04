from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    textnode.__repr__()

    print("")
    
    htmlnode = HTMLNode("p", "lolparagraaf", None, {"href": "https://www.google.com", "target": "_blank"})
    htmlnode.__repr__()
    print(htmlnode.props_to_html())



if __name__ == "__main__":
    main()