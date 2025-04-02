
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.zro2xp.me")
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()

    print(text_node)
    print(node)

main()
