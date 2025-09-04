import unittest

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