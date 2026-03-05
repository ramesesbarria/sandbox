from utils.helper import multiTableBlockFinder
from utils.helper import setTableRowHeight, getTableRowHeightCM, setRowParagraphFont
from utils.helper import iterBlockItems
from utils.log import log_message

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

def editPFTableProperties(document):

	#find clients name to find clients profile table and add it to TABLE_IDENTIFIERS
	for block in iterBlockItems(document):

		if isinstance(block, Paragraph):
			clientFName = re.search(r"Dear\s+([A-Za-z\.\- ]+),?", block.text)
			if clientFName:
				clientName = clientFName.group(1).strip()

				newIdentifier = tuple(["Description", clientName])
				newValue = {
					"name": "Profile Table",
					"process": 1,
					"processDescription": "Your personal and financial position",
				}
				TABLE_IDENTIFIERS[tuple(newIdentifier)] = newValue
				break 

	#find all table from TABLE_IDENTIFIERS and save it to table list
	tableList = multiTableBlockFinder(document, TABLE_IDENTIFIERS)

	if tableList:
		#process all tablelist
		for table in tableList:
			for row in table.rows:
				setTableRowHeight(row, 0.6)
				setRowParagraphFont(row, 9)
	else:
		State.notRunProgress = State.notRunProgress + "\n1 editPFTableProperties target"

	
