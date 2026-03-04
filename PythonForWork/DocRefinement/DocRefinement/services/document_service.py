# services/document_service.py

from state import State
from utils.helper import open_doc, save_doc
from utils.log import log_message

from services.fix_table import fix_fragmented_tables
from services.personal_financial import format_personal_financial_section
from services.risk_profile import update_risk_portfolio_section
from services.investment_portfolio_recommendation import (
    format_investment_portfolio_recommendation_section,
    modify_mda_service_fee_section,
    move_invesment_management_fees_section,
    move_sales_and_purchases_section,
    move_proposed_portfolio_section,
)

from services.CostComparison import change_cost_comparison_section
from services.ProposedAsset import modify_proposed_asset_section
from services.AppendixFinancialProjections import modify_appendix_financial_projections_section
from services.key_assumptions import modify_key_assumptions_section
from services.consolidated_cash_flow import modify_consolidated_cashflow_section
from services.CleanUp import cleanup_cash_flow_section

from services.estate_planning import process_estate_planning_section
from services.in_brief_estate_planning import process_in_brief_estate_planning
from services.estate_planning_recommendations import update_estate_planning_recommendations


def update_document_workflow(documentName):
    """
    Executes the full document modification workflow.
    Design to target modification step by step base on requirements 
    for ease management and updating. 

    Args:
        documentName (str): Full document filename including extension.

    Returns:
        str: Result message or document name.
    """

    document = open_doc(documentName)
    print(document)
    # State.docname = document

    if document is None:
        return f"Document {documentName} cannot be found!"

    # Fix fragmented tables caused by document parsing
    working_doc  = fix_fragmented_tables(document)




    # --------------------- SOA OLD -------------------- #


    # Requirement 1: Personal and financial position
    format_personal_financial_section(working_doc)

    # Requirement 2: Risk Profile
    # Blockers on spell checks
    update_risk_portfolio_section(working_doc)

    # Requirement 3: Investment Portfolio recommendations
    # Requirement 3.1 - 3.4: Proposed Investment Portfolio
    # Currently not able to fix Issue results from fix_fragmented_tables
    # Issue row with singles cell will now expand
    # For text color modification clarification on mix color
    format_investment_portfolio_recommendation_section(working_doc)
    # Requirement 3.5 Remove and move sections
    modify_mda_service_fee_section(working_doc)
    # Requirement 3.5.1. Investment Management Fees and Buy/Sell Spreads 
    move_invesment_management_fees_section(working_doc)
    # Requirement 3.5.2. Sales and Purchases
    move_sales_and_purchases_section(working_doc)
    # Requirement 3.5.3. Propose Portfolio/s 
    move_proposed_portfolio_section(working_doc)
    # Requirement 3.6. Add page breaks 
    # Requirement 3.6.1. Cost Comparison
    change_cost_comparison_section(working_doc)
    # Requirement 3.6.2. Your Proposal Asset Allocation 
    modify_proposed_asset_section(working_doc)
 
    # Requirement 4. Appendix  
    # Requirement 4.1. Financial Projections  
    # Requirement 4.1.1. Investment Assumptions 
    modify_appendix_financial_projections_section(working_doc)
    # Requirement 4.1.2. Key Assumptions
    modify_key_assumptions_section(working_doc)
    # Requirement 4.1.3. Consolidated Cashflow
    modify_consolidated_cashflow_section(working_doc)
    cleanup_cash_flow_section(working_doc)

     # --------------------- SOA NEW -------------------- #

       # Requirement 1.1 - Testamentary Trust
    is_testamentary = process_estate_planning_section(working_doc)

    # Requirement 1.2 + 1.3 - In Brief Estate Planning
    process_in_brief_estate_planning(working_doc, is_testamentary)

    # Requirement 1.4 - Estate Planning Recommendations Section
    update_estate_planning_recommendations(working_doc, is_testamentary)


    save_doc(working_doc, documentName)

    if State.notRunProgress != 'target not found and ff process not run: ':
        log_message(State.notRunProgress)
        return f"Unprocessed logs: {State.notRunProgress}"

    return documentName
