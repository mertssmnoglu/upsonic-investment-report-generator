from upsonic import Task
from tools.http import yFinance
from tasks.new import new_save_report_task

from dotenv import load_dotenv
from os import getenv

load_dotenv()

stock_market_analysis_for_ticker = Task(
    f"Generate comprehensive stock market analysis report in markdown format for {getenv('TICKER')}",
    tools=[yFinance],
)

save_report = new_save_report_task()
save_report.context = [stock_market_analysis_for_ticker]


stock_analyst_task_list = [stock_market_analysis_for_ticker, save_report]
