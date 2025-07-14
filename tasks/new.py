from upsonic import Task
from tools.stdio import Reports
from tools.http import yFinance


def newStockMarketAnalysisTask(tickers: str):
    return Task(
        f"Generate comprehensive stock market analysis report in markdown format for {tickers}",
        tools=[yFinance],
    )


def new_save_report_task() -> Task:
    return Task(
        "Only save the report under the 'reports' directory in markdown format.",
        tools=[Reports.create_markdown_report],
    )
