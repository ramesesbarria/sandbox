from utils.helper import multi_table_block_finder
from utils.helper import set_table_row_height, set_row_paragraph_font
from utils.helper import iter_block_items

from docx.text.paragraph import Paragraph
import re
from state import State

TABLE_IDENTIFIERS = {
    tuple(["Name", "Date of birth", "Dependent until age"]): {
		"name": "Dependants Table",
        "process": 1,
		"processDescription": "Your personal and financial position",
	},

    tuple(["Income", "Owner", "Amount (p.a.)"]): {
		"name": "Income Table",
        "process": 1,
		"processDescription": "Your personal and financial position",
	},
    tuple(["Expense", "Owner", "Amount (p.a.)"]): {
		"name": "Expenditure Table",
        "process": 1,
		"processDescription": "Your personal and financial position",
	},

    tuple(["Description", "Owner", "Amount"]): {
		"name": "Assets and Liabilities Table (Assets)",
        "process": 1,
		"processDescription": "Your personal and financial position",
	},

    tuple(["Description", "Owner", "Balance", "Death", "TPD", "Inc Prot"]): {
		"name":"Superannuation Funds Table",
        "process": 1,
		"processDescription": "Your personal and financial position",
	},

    tuple(['Description', 'Description']): {
		"name":"Personal Insurance Policies Table",
        "process": 1,
		"processDescription": "Your personal and financial position",
	}
}

def format_personal_financial_section(document):
	"""
	Modify Personal and financial position Table Properties
	Using tuple as identifier to search table header
	update all table height to 0.6 and font size 9
	"""
				
	for block in iter_block_items(document):

		if isinstance(block, Paragraph):

			"""
			Modify Personal and financial position Table Properties
			
			"""
			client_full_name = re.search(r"Dear\s+([A-Za-z\.\- ]+),?", block.text)
			
			if client_full_name:
				clientName = client_full_name.group(1).strip()

				newIdentifier = tuple(["Description", clientName])
				newValue = {
					"name": "Profile Table",
					"process": 1,
					"processDescription": "Your personal and financial position",
				}
				TABLE_IDENTIFIERS[tuple(newIdentifier)] = newValue
				break 

	#find all table from TABLE_IDENTIFIERS and save it to table list
	tableList = multi_table_block_finder(document, TABLE_IDENTIFIERS)

	if tableList:
		#process all tablelist
		for table in tableList:
			for row in table.rows:
				set_table_row_height(row, 0.6)
				set_row_paragraph_font(row, 9)
	else:
		State.notRunProgress = State.notRunProgress + "\n" + State.docname + " 1 Your personal and financial position "

	
