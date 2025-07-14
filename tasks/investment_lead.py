from upsonic import Task
from tasks.new import new_save_report_task
from tasks.research_analyst import research_rank_companies

generate_complete_investment_report = Task(
    "As an Invesment Leader, generate complete investment report in markdown format",
    context=[research_rank_companies],
)

save_report = new_save_report_task()
save_report.context = [generate_complete_investment_report]

investment_lead_task_list = [research_rank_companies, save_report]
