
from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.zro2xp.me")

    print(text_node)

main()
