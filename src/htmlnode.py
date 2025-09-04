

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not implemented yet")
    
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