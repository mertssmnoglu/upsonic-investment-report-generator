# Tasks
import tasks.stock_analyst
import tasks.research_analyst
import tasks.investment_lead

# Tools
# from tools.mcp import something


stock_analyst_task_list = [
    tasks.stock_analyst.stock_market_analysis_for_ticker,
    tasks.stock_analyst.save_report,
]


research_analyst_task_list = [
    tasks.research_analyst.research_rank_companies,
    tasks.research_analyst.save_report,
]


investment_lead_task_list = [
    tasks.investment_lead.generate_complete_investment_report,
    tasks.investment_lead.save_report,
]
