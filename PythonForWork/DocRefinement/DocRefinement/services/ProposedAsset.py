from utils.helper import set_table_row_height

from utils.helper import iter_block_items
from docx.text.paragraph import Paragraph
from docx.table import Table
import re
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm
from state import State

def modify_proposed_asset_section(document):

	inside = False
	success = False
	percentageColumnWidth = Cm(3)
	rateColumnWidth = Cm(5)

	for block in iter_block_items(document):

		if isinstance(block, Paragraph):
			startBlock = re.search(r"Your Proposed Asset Allocation", block.text, re.IGNORECASE)
			endBeforeBlock = re.search(r"Estate planning recommendations", block.text, re.IGNORECASE)
			if startBlock:
				inside = True
			if endBeforeBlock:
				inside = False
			if inside:
				for run in block.runs:
					if run.element.xpath('.//pic:pic'):
						block.alignment = WD_ALIGN_PARAGRAPH.CENTER
		elif inside and isinstance(block, Table):
			for i, row in enumerate(block.rows):
				if i != 0:  # skip header row
					set_table_row_height(row, 0.6)

				if len(row.cells) == 8:
					for idx, cell in enumerate(row.cells):
							grid_span = 1
							# Assign width based on logical position
							if idx == 2 or idx >= 4:
								cell.width = percentageColumnWidth
							else:
								cell.width = rateColumnWidth

			success = True

	if not success:
		State.notRunProgress = State.notRunProgress + "\n" + State.docname + " 3.5.2. Sales and Purchases"

