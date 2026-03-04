from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn
from utils.helper import find_tables_by_top_leftcells
from utils.helper import iter_block_items 

TABLE_IDENTIFIERS = {
    tuple(["Date","Age"]): {
		"name": "Consolidated CashFlow and Assets Table",
        "process": "4.1.3",
		"processDescription": "Your personal and financial position",
	}
}

def is_paragraph_empty(p: Paragraph) -> bool:
    """
    Returns True if paragraph has no visible text (including runs with only whitespace).
    Ignores all formatting, page breaks, tabs, and empty runs.
    """
    if not p.text or p.text.strip() == "":
        return True
    return False


def remove_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    paragraph._p = paragraph._element = None



def cleanup_cash_flow_section(document):
    
    blocks = list(iter_block_items(document))
    target_table_count = 0

    # using loop instead iteritation using item to Freeze blocks (CRITICAL)
    for i, block in enumerate(blocks):
        if not isinstance(block, Table):
            continue

        # Check if this is one of your target tables
        if not find_tables_by_top_leftcells(block, TABLE_IDENTIFIERS):
            continue
        
        target_table_count += 1

        # Skip cleanup for the second target table
        if target_table_count <= 2:
            continue

        j = i + 1
        empty_paragraphs = []

        # Collect ONLY consecutive empty paragraphs
        while j < len(blocks):
            b = blocks[j]

            if isinstance(b, Paragraph) and is_paragraph_empty(b):
                empty_paragraphs.append(b)
                j += 1
                continue

            break  # first real content reached

        # # Debug (this should now be stable)
        # print("\nTARGET TABLE FOUND")
        # print(f"Empty paragraphs after table: {len(empty_paragraphs)}")

        # if j < len(blocks) and isinstance(blocks[j], Paragraph):
        #     print(f"Next real paragraph: {blocks[j].text}")

        # Remove the faulty paragraphs
        for p in empty_paragraphs:
            remove_paragraph(p)