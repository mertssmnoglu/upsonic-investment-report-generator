from upsonic import Task
from os import getenv
from tools.stdio import Reports
from tools.http import yFinance
# from tools.mcp import something


__stock_market_analysis_for_ticker = Task(
    f"Generate comprehensive stock market analysis report in markdown format for {getenv('TICKER')}",
    # response_format=FinanceSearchResult,
    tools=[yFinance],
)

__research_rank_companies = Task(
    "Rank companies and generate detailed investment analysis and ranking report in markdown format",
    context=[__stock_market_analysis_for_ticker],
)

__investment_lead = Task(
    "As an Invesment Leader, generate complete investment report in markdown format",
    context=[__research_rank_companies],
)


# ==============#
# Report Saving #
# ==============#

__save_report_stock = Task(
    """
Only save the report under the "reports" directory in markdown format.  
""",
    tools=[Reports.create_markdown_report],
    context=[
        __stock_market_analysis_for_ticker,
    ],
)

__save_report_research = Task(
    """
Only save the report under the "reports" directory in markdown format.  
""",
    tools=[Reports.create_markdown_report],
    context=[
        __research_rank_companies,
    ],
)

__save_report_investment = Task(
    """
Only save the report under the "reports" directory in markdown format.  
""",
    tools=[Reports.create_markdown_report],
    context=[
        __investment_lead,
    ],
)


# ===========#
# Task Lists #
# ===========#

stock_analyst = [__stock_market_analysis_for_ticker, __save_report_stock]
research_analyst = [__research_rank_companies, __save_report_research]
investment_lead = [__investment_lead, __save_report_investment]
