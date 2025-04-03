
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.zro2xp.me")
    node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]).to_html()

    print(text_node)
    print(node)

main()
