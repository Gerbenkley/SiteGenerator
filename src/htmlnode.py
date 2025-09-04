class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not yet implemented")
    
    def props_to_html(self):
        if not self.props:
            return ""
        parts = []
        for key in sorted(self.props.keys()):
            parts.append(f' {key}="{self.props[key]}"')
        return "".join(parts)
    
    def __repr__(self):
        return print(
            f" tag: {self.tag}\n", 
            f"value = {self.value}\n", 
            f"children = {self.children}\n", 
            f"props = {self.props}\n"
            )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=(), props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not children:
            raise ValueError("ParentNode must have children nodes.")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if not self.children:
            raise ValueError("ParentNode must have children nodes.")
        
        parts = []
        for child in self.children:
            parts.append(child.to_html())
        inner_html = "".join(parts)

        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"