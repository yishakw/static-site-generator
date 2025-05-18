# import unittest
from markdowntoblocks import markdown_to_blocks
# class MarkdownToBlocksTest(unittest.TestCase):
#     def test_markdown_to_blocks(self):
#         md = """ 
#         This is **bolded** paragraph

#         This is another paragraph with _italic_ text and `code` here
#         This is the same paragraph on a new line

#         - This is a list
#         - with items
#         """
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#                 "- This is a list\n- with items",
#             ],
#         )
#     def test_markdown_to_blocks_empty(self):
#         md = ""
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(blocks, [])    
#     def test_markdown_to_blocks_no_newline(self):
#         md = "This is a single line of text"
#         blocks = markdown_to_blocks(md)
#         self.assertEqual(blocks, ["This is a single line of text"])
import unittest
import textwrap

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = textwrap.dedent("""
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
        """).strip()

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
