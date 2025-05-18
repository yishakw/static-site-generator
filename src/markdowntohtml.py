from markdowntoblocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
from parentnode import ParentNode
from markdowntoblocks import BlockType
from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from splitdelimitter import text_to_textnodes
# from textnode import TextNode, TextType  

# def markdown_to_html(markdown):
#     blocks = markdown_to_blocks(markdown)
#     for block in blocks:
#         block_type = block_to_block_type(block)
#         if block_type == "paragraph":
#             html_node = HTMLNode(tag="p", value=block)
#         elif block_type == "header":
#             level = block.count("#")
#             html_node = HTMLNode(tag=f"h{level}", value=block[level:].strip())
#         elif block_type == "quote":
#             html_node = HTMLNode(tag="blockquote", value=block[1:].strip())
#         elif block_type == "unordered_list":
#             items = block.split("\n")
#             html_node = HTMLNode(tag="ul", children=[HTMLNode(tag="li", value=item[2:]) for item in items])
#         elif block_type == "ordered_list":
#             items = block.split("\n")
#             html_node = HTMLNode(tag="ol", children=[HTMLNode(tag="li", value=item[2:]) for item in items])
#         elif block_type == "code":
#             # Assuming code blocks are wrapped in triple backticks
#             html_node = HTMLNode(tag="code", value=block)
#         else:
#             html_node = HTMLNode(value=block)
# def text_to_children(text):
#     lines = text.split("\n")
#     children = []
#     for line in lines:
#         if line.strip():
#             children.append(HTMLNode(tag="p", value=line.strip()))
#     return children
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)