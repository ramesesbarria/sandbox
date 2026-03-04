
from utils.helper import add_breaks_in_between_paragraph
from state import State

def change_cost_comparison_section(document):    
    START_MARKER = "Cost comparison"
    END_MARKER   = "MDA Service fee"

    success = add_breaks_in_between_paragraph(document, START_MARKER, END_MARKER)
    if not success:
        State.notRunProgress = State.notRunProgress + "\n" + State.docname + " 3.5.2. Sales and Purchases"