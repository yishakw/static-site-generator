from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newTXT= []
    for node in old_nodes:
        # for word, i in node.text.split():
        #     if delimiter in word:
        #         newTXT.append(node[:i])
        newT = node.text.split(delimiter)
        for txt in newT:
            # if delimiter in txt:
            # if f"{delimiter}{txt}{delimiter}" in node.text:
            if re.findall(rf"{delimiter}{txt}{delimiter}", node.text):
                newTXT.append(TextNode(txt, text_type))
            else:
                newTXT.append(TextNode(txt, TextType.TEXT))
    return newTXT
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# print(new_nodes)
def extract_markdown_images(text):
    return re.findall(r'!\[(.*?)\]\((.*?)\)', text)
def extract_markdown_links(text):   
    return re.findall(r'\[(.*?)\]\((.*?)\)', text)

def split_nodes_image(old_nodes):
    newTXT = []
    pattern = r'\[[^\]]+\]\([^)]+\)|[^\[]+'
    for node in old_nodes:
        parts = re.findall(pattern, node.text)
        for part in parts:
            if part.startswith('[') and ']' in part and '(' in part and part.endswith(')'):
                text, url = re.findall(r'\[(.*?)\]\((.*?)\)', part)[0]
                newTXT.append(TextNode(text, TextType.IMAGE, url))
            else:
                newTXT.append(TextNode(part, TextType.TEXT))
    return newTXT
def split_nodes_link(old_nodes):
    newTXT = []
    pattern = r'\[[^\]]+\]\([^)]+\)|[^\[]+'
    for node in old_nodes:
        parts = re.findall(pattern, node.text)
        for part in parts:
            if part.startswith('[') and ']' in part and '(' in part and part.endswith(')'):
                text, url = re.findall(r'\[(.*?)\]\((.*?)\)', part)[0]
                newTXT.append(TextNode(text, TextType.LINK, url))
            else:
                newTXT.append(TextNode(part, TextType.TEXT))
    return newTXT
def text_to_textnodes(text):
    # Split the text into parts based on the delimiters
    parts = re.split(r'(\*\*.*?\*\*|__.*?__|\*\*.*?\*\*|__.*?__|`.*?`)', text)
    # Create a list to hold the TextNode objects
    text_nodes = []
    # Iterate through the parts and create TextNode objects
    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            text_nodes.append(TextNode(part[2:-2], TextType.BOLD))
        elif part.startswith('__') and part.endswith('__'):
            text_nodes.append(TextNode(part[2:-2], TextType.ITALIC))
        elif part.startswith('`') and part.endswith('`'):
            text_nodes.append(TextNode(part[1:-1], TextType.CODE))
        else:
            text_nodes.append(TextNode(part, TextType.TEXT))
    return text_nodes