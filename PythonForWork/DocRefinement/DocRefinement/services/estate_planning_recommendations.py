from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.shared import RGBColor, Pt
from utils.helper import iter_block_items
from utils.log import log_message
from state import State

BLACK = RGBColor(0x00, 0x00, 0x00)

START_MARKER = 'Estate planning recommendations'
END_MARKER   = 'Projected outcomes'


# ── Read estate planning entries from Personal Details table ──────────────────

def _read_estate_planning_entries(document):
    entries = {'will': None, 'poa': None, 'guardianship': None}
    ROW_MAP = {
        'do you have a will?':         'will',
        'enduring power of attorney?': 'poa',
        'enduring guardianship?':      'guardianship',
    }
    for table in document.tables:
        for row in table.rows:
            first_cell = row.cells[0].text.strip().lower()
            key = ROW_MAP.get(first_cell)
            if key and len(row.cells) > 1:
                entries[key] = row.cells[1].text.strip()
    return entries


# ── Phrase builders ───────────────────────────────────────────────────────────

def _will_phrase(will_value):
    return 'your Will reviewed' if will_value == 'Yes' else 'a Will prepared'

def _poa_phrase(poa_value):
    return 'review your' if poa_value == 'Yes' else 'establish an'


# ── Step 2: Set spacing 6pt before/after on ALL paragraphs in section ─────────

def _set_section_spacing(document):
    inside = False
    count = 0

    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            if block.text.strip() == START_MARKER:
                inside = True
            if inside and block.text.strip() == END_MARKER:
                break
            if inside:
                block.paragraph_format.space_before = Pt(6)
                block.paragraph_format.space_after  = Pt(6)
                count += 1

    log_message(f"Estate Planning Recs: set 6pt spacing on {count} paragraphs.")


# ── Steps 6 + 8: Update main recommendation paragraph ────────────────────────

def _update_recommendation_paragraph(document, entries):
    """
    Finds the main 'We recommend you have...' paragraph in the
    Estate planning recommendations section and:
      - Step 6: Replaces red placeholder phrases based on Yes/No entries
      - Step 8: Sets all runs to black
    Note: testamentary trust runs are already cleared by estate_planning.py
    """
    inside = False
    success = False

    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            if block.text.strip() == START_MARKER:
                inside = True
            if inside and block.text.strip() == END_MARKER:
                break

            if inside and block.text.startswith('We recommend you have'):
                runs = block.runs

                if len(runs) < 5:
                    log_message("Estate Planning Recs: Unexpected run count in main paragraph.")
                    State.notRunProgress += '\n' + State.docname + ' 1.4. Estate Planning Recs - Unexpected run structure'
                    return

                # Step 6 — replace red placeholders
                runs[1].text = _will_phrase(entries.get('will'))
                runs[3].text = _poa_phrase(entries.get('poa'))

                # Step 8 — all runs to black
                for run in block.runs:
                    run.font.color.rgb = BLACK

                success = True
                break

    if not success:
        log_message("Estate Planning Recs: Main recommendation paragraph not found.")
        State.notRunProgress += '\n' + State.docname + ' 1.4. Estate Planning Recs - Main paragraph not found'


# ── Step 5 (1.4.1): Remove all empty paragraphs in the section ───────────────

def _remove_empty_paragraphs(document):
    inside = False
    to_remove = []

    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            if block.text.strip() == START_MARKER:
                inside = True
            if inside and block.text.strip() == END_MARKER:
                break
            if inside and block.text.strip() == '':
                to_remove.append(block)

    for para in to_remove:
        p = para._element
        p.getparent().remove(p)

    log_message(f"Estate Planning Recs: removed {len(to_remove)} empty paragraphs.")


# ── Entry point ───────────────────────────────────────────────────────────────

def update_estate_planning_recommendations(document, testamentary_trust_yes):
    """
    Main entry point called from document_service.py.

    Args:
        document: open SOA Document object
        testamentary_trust_yes (bool): True if Paraplanning form checkbox = Yes
                                       (unused here - testamentary removal handled
                                        by estate_planning.py earlier in pipeline)
    """
    entries = _read_estate_planning_entries(document)

    # Step 2 — spacing
    _set_section_spacing(document)

    # Steps 6 + 8 — update main paragraph
    # Note: Step 7 (testamentary trust removal) is already handled by
    # estate_planning.py which runs earlier in the pipeline
    _update_recommendation_paragraph(document, entries)

    # 1.4.1 Step 5 — remove empty paragraphs
    # Note: <if testamentary trust> bullet removal also already handled
    # by estate_planning.py
    _remove_empty_paragraphs(document)