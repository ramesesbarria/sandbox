from utils.helper import multi_table_block_finder

from utils.helper import iter_block_items
from docx.text.paragraph import Paragraph
import re
from docx.shared import Pt
from state import State

TABLE_IDENTIFIERS = {
	tuple(['Portfolio', 'Risk profile']): {
		"name":"Risk Porfolio Table",
        "process": 2,
		"processDescription": "Risk profile",
	}
}


def update_risk_portfolio_section(document):
	"""
	Modify Risk profile Table Properties
	Using tuple as identifier to search table header
	
	Found table will be one of the basis for modification on paragraph.
	"""

	#find profileTable
	profileTable = multi_table_block_finder(document, TABLE_IDENTIFIERS)
	
	#list all block with Profile(s)
	ParagraphBlocksList = []

	if profileTable:
		
		for block in iter_block_items(document):
			if isinstance(block, Paragraph):
				blockWithProfile = re.search(r"profile\(s\)", block.text, re.IGNORECASE)
				
				if blockWithProfile:
					ParagraphBlocksList.append(block)

		if ParagraphBlocksList:
			#Update paragragph text if profile table is below 2 means 1 record of client only
			if len(profileTable[0].rows) <= 2:
				for paragraph in ParagraphBlocksList:
					updatedText = re.sub(r'\bprofile\(s\)', 'profile', paragraph.text)
					
					if updatedText != paragraph.text:
						paragraph.text = updatedText

			#Update add space base on requirements.
			ParagraphBlocksList[0].paragraph_format.space_before = Pt(6)
			ParagraphBlocksList[0].paragraph_format.space_after = Pt(6)
		else:
			State.notRunProgress = State.notRunProgress + "\n" + State.docname + " 1 Risk Profile "
	else:
		State.notRunProgress = State.notRunProgress + "\n" + State.docname + " 1 Risk Profile "