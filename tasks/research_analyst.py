from upsonic import Task
from tasks.new import new_save_report_task
from tasks.stock_analyst import stock_market_analysis_for_ticker

from dotenv import load_dotenv

load_dotenv()

research_rank_companies = Task(
    "As a researcher, rank the companies and generate detailed 'investment analysis and ranking' report in markdown format",
    context=[stock_market_analysis_for_ticker],
)

save_report = new_save_report_task()
save_report.context = [research_rank_companies]

research_analyst_task_list = research_rank_companies, save_report
