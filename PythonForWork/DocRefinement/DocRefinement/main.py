from services.document_service import update_document_workflow

def update_doc(docname):
    """
    Automation Anywhere entrypoint.

    Args:
        docname (str): Document name without extension.

    Returns:
        str: Result message for Automation Anywhere.
    """
    
    documentName = docname + ".docx"

    return update_document_workflow(documentName)


# running as a script for testing
if __name__ == "__main__":

    # docName = 'Mr Joe Goon - (SOA) - 11 November 2025'
    # docName = 'Ms Laura Glik - (SOA) - 12 May 2025 (1)'
    # docName = 'Ms Laura Glik - (SOA) - 12 May 2025 (2)'
    docName = 'Mr Andrew Stamper - (SOA) - 9 February 2026 1'


    

    update_doc(docName)

