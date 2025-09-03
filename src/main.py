from textnode import TextType, TextNode

def main():
    Node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    Node.__repr__()



if __name__ == "__main__":
    main()