from docx import Document
from docx.text.paragraph import Paragraph
from utils.helper import iter_block_items
from utils.log import log_message
from state import State
from config import DOC_PATH

W14 = 'http://schemas.microsoft.com/office/word/2010/wordml'


def read_testamentary_trust_checkbox(form_doc):
    """
    Reads the Paraplanning Request Form and returns True if 
    'Are we recommending a testamentary trust?' is checked Yes, False if No.
    Returns None if the row cannot be found.
    """
    for table in form_doc.tables:
        for row in table.rows:
            row_text = ' '.join(c.text.strip() for c in row.cells).lower()
            if 'are we recommending a testamentary trust' in row_text:
                checkboxes = row._tr.findall(f'.//{{{W14}}}checkbox')
                if len(checkboxes) >= 1:
                    # First checkbox = Yes, Second checkbox = No
                    yes_checked_elem = checkboxes[0].find(f'{{{W14}}}checked')
                    if yes_checked_elem is not None:
                        val = yes_checked_elem.get(f'{{{W14}}}val')
                        return val == '1'  # True = Yes checked, False = No checked
    return None


def remove_testamentary_trust_content(soa_doc):
    """
    Removes testamentary trust content from the SOA document:
    1. Removes all bullet paragraphs starting with '<if testamentary trust>'
    2. Removes the inline testamentary trust sentence from the main paragraph
    """
    paragraphs_to_remove = []

    for block in iter_block_items(soa_doc):
        if not isinstance(block, Paragraph):
            continue

        # --- Remove full bullet paragraphs tagged <if testamentary trust> ---
        if block.text.strip().lower().startswith('<if testamentary trust>'):
            paragraphs_to_remove.append(block)
            continue

        # --- Remove inline testamentary trust runs from the main paragraph ---
        if block.text.startswith('We recommend you have') and 'testamentary' in block.text.lower():
            runs_to_clear = []
            for run in block.runs:
                if 'testamentary trust' in run.text.lower():
                    runs_to_clear.append(run)
                # Also remove the follow-on sentence that starts with " As part of reviewing"
                elif run.text.strip().startswith('As part of reviewing your Will') and 'testamentary trust provision' in run.text.lower():
                    runs_to_clear.append(run)

            for run in runs_to_clear:
                run.text = ''

    # Remove tagged paragraphs
    removed_count = 0
    for para in paragraphs_to_remove:
        p = para._element
        p.getparent().remove(p)
        removed_count += 1

    return removed_count


def process_estate_planning_section(soa_doc):
    """
    Main entry point.
    Opens the Paraplanning Request Form, checks the testamentary trust checkbox,
    and conditionally removes content from the SOA document.
    """
    try:
        form_path = DOC_PATH + 'Paraplanning Request Form.docx'
        form_doc = Document(form_path)
    except Exception as e:
        log_message(f"Estate Planning: Could not open Paraplanning Request Form - {e}")
        State.notRunProgress += '\n' + State.docname + ' 1.1. Testamentary Trust - Could not open Paraplanning Request Form'
        return False

    is_testamentary_trust = read_testamentary_trust_checkbox(form_doc)

    if is_testamentary_trust is None:
        log_message("Estate Planning: Could not find testamentary trust checkbox in Paraplanning Request Form")
        State.notRunProgress += '\n' + State.docname + ' 1.1. Testamentary Trust - Checkbox not found'
        return False

    if is_testamentary_trust:
        # Yes - keep everything, nothing to do
        log_message("Estate Planning: Testamentary trust = Yes. Keeping all estate planning content.")
        return True

    # No - remove testamentary trust content
    removed = remove_testamentary_trust_content(soa_doc)
    log_message(f"Estate Planning: Testamentary trust = No. Removed {removed} tagged paragraphs and inline sentence.")
    return False