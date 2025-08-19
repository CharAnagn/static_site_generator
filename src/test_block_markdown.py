import unittest

from block_markdown import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Smallest heading"), BlockType.HEADING)
        # Not a heading (missing space)
        self.assertEqual(block_to_block_type("###Not heading"), BlockType.PARAGRAPH)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```print('hi')```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\nline1\nline2\n```"), BlockType.CODE)
        # Not a code block (only two backticks)
        self.assertEqual(block_to_block_type("`` not code ``"), BlockType.PARAGRAPH)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> a\n> b"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> single line quote"), BlockType.QUOTE)
        # Not all lines start with >
        self.assertEqual(block_to_block_type("> one\nnot quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item1\n- item2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- only one item"), BlockType.UNORDERED_LIST)
        # Missing space after dash
        self.assertEqual(block_to_block_type("-not valid"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. one\n2. two\n3. three"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. start"), BlockType.ORDERED_LIST)
        # Wrong numbering (skips 2)
        self.assertEqual(block_to_block_type("1. one\n3. three"), BlockType.PARAGRAPH)
        # Wrong numbering (starts at 2)
        self.assertEqual(block_to_block_type("2. wrong start"), BlockType.PARAGRAPH)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("with *markdown* inside but still paragraph"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
