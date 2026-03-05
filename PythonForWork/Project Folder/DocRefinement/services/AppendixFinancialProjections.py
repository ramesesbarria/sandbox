from utils.helper import set_table_row_height
from utils.helper import is_row_blank, delete_row
from utils.helper import iter_block_items

from docx.text.paragraph import Paragraph
from docx.table import Table
import re
from docx.enum.text import WD_ALIGN_PARAGRAPH
from state import State


def modify_appendix_financial_projections_section(document):

	inside = False
	success = False
	
	for block in iter_block_items(document):

		if isinstance(block, Paragraph):
			startBlock = re.search(r"Appendix: Financial projections", block.text, re.IGNORECASE)
			endBeforeBlock = re.search(r"Appendix: Insurance quotations", block.text, re.IGNORECASE)
			if startBlock:
				inside = True
			if endBeforeBlock:
				inside = False
				
		elif inside and isinstance(block, Table):
			for i, row in enumerate(block.rows):
				set_table_row_height(row, 0.6)
				if is_row_blank(row) and i != 0:
					delete_row(block, row)
				
				for idx, cell in enumerate(row.cells):
					# Left-align the FIRST cell
					if idx == 0:
						for paragraph in cell.paragraphs:
							paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

					# Right-align ALL other cells
					else:
						for paragraph in cell.paragraphs:
							paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

			success = True

	if not success:
		State.notRunProgress = State.notRunProgress + "\n" + State.docname + " 4.1.1. Investment Assumptions"

