import re
from enum import Enum
def markdown_to_blocks(markdown):
    blks = markdown.strip().split("\n\n")
    return [block.strip() for block in blks]
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.strip().split("\n")

    # Check for code block
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    # Check for heading
    if re.match(r"#{1,6} ", lines[0]):
        return BlockType.HEADING

    # Check for quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Check for ordered list
    if all(re.match(rf"{i+1}\. ", lines[i]) for i in range(len(lines))):
        return BlockType.ORDERED_LIST

    # Default to paragraph
    return BlockType.PARAGRAPH
