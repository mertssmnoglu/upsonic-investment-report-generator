from upsonic import Task
from tools import WriteContentToFile, YFinanceTool

# from tasks import research_on_yfinance_task
from pydantic import BaseModel

# Agents
from agents import stock_analyst
# from agents import research_analyst
# # from agents import investment_lead
# from agents import agent
# from agents import reliable_agent


class FinanceSearchResult(BaseModel):
    """
    Base Model for Finance Search Result

    Use json() method when you need json.
    """

    fullname: str
    symbol: str
    city: str
    summary: str
    sector: str
    last_50_day_average: str
    last_200_day_average: str
    data_source: str
    previous_close: str
    analyst_recommendation: str
    total_cash: int


# Workflow
symbol = input("Symbol to research: ")

task = Task(
    "Research for given symbol and save the report as 'report.json' with corrected json format using WriteContentToFile",
    response_format=FinanceSearchResult,
    tools=[
        WriteContentToFile,
        YFinanceTool,
    ],
    context=[symbol],
)

stock_analyst.print_do(task)
