from docx.table import Table
from docx.text.paragraph import Paragraph
from copy import deepcopy
from utils.helper import iterBlockItems, addCellToHeader, mergeCellsRange, alignCellText
from utils.helper import multiTableBlockFinder, multiTableBlockFinderWithTag

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches

TABLE_IDENTIFIERS = {
    tuple(['Investment', 'Amount', 'Sell cost']): {
		"name":"Fix Issues encounter in merge multiple split table",
        "process": 4,
		"processDescription": "Fix Issues encounter in merge multiple split",
	},
	tuple(['Investment', 'Amount', 'Buy cost']): {
		"name":"Fix Issues encounter in merge multiple split table",
        "process": 4,
		"processDescription": "Fix Issues encounter in merge multiple split",
	},
	tuple(['Investment', 'Amount', 'Ongoing Investment\nManagement Fees']): {
		"name":"Fix Issues encounter in merge multiple split table",
        "process": 4,
		"processDescription": "Fix Issues encounter in merge multiple split",
	},
}


def FixTableIssue(document):
    datas = multiTableBlockFinderWithTag(document, TABLE_IDENTIFIERS)
   
    for data in datas:
        table = data[0]
        addCellToHeader(table.rows[0], new_header_text="Extra Column")
        mergeCellsRange(table.rows[0],2,3,10)
        
        # print(len(mergeRow.cells))
        if data[1] == "Ongoing Investment\nManagement Fees":
            alignCellText(table.rows[0], -1, alignment=WD_ALIGN_PARAGRAPH.RIGHT)

            addCellToHeader(table.rows[-1], new_header_text="Extra Column")
            mergeCellsRange(table.rows[-1],2,3,10)
            alignCellText(table.rows[-1], -1, alignment=WD_ALIGN_PARAGRAPH.RIGHT)

            addCellToHeader(table.rows[-2], new_header_text="Extra Column")
            mergeCellsRange(table.rows[-2],2,3,10)
            alignCellText(table.rows[-2], -1, alignment=WD_ALIGN_PARAGRAPH.RIGHT)
            
        elif data[1]  == "Sell cost" or data[1] == "Buy cost":
            alignCellText(table.rows[0], -1, alignment=WD_ALIGN_PARAGRAPH.CENTER)

        for row in table.rows:
            if len(row.cells) > 3:
                row.cells[3].width = Inches(1)


def fixSplitTables(doc, merge_condition=None):

    block_list = list(iterBlockItems(doc))

    i = 0

    tables_to_remove = []
    
    while i < len(block_list):
        block = block_list[i]

        if isinstance(block, Table):


            # Keep merging following tables as long as they are consecutive
            j = i + 1
            while j < len(block_list) and isinstance(block_list[j], Table):
                next_table = block_list[j]
                # Append all rows from next_table to current table
                for row in next_table.rows:
                    new_row = deepcopy(row._tr)
                    block._tbl.append(new_row)
                tables_to_remove.append(next_table)
                j += 1
            i = j  # Skip merged tables
        else:
            i += 1

    # Remove merged tables from the document
    for t in tables_to_remove:
        t._element.getparent().remove(t._element)


    FixTableIssue(doc)



    return doc