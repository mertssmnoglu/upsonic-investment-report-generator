import tasks.list as task_list

from workflow import Workflow

# Agents
from agents import stock_analyst, research_analyst, investment_lead

workflow = Workflow(
    name="Investment Report Generator",
    description="Investment Report Generator Workflow Example with Upsonic",
    timeout=1,  # 1 second timeout between each agent
    entries=[
        {
            "agent": stock_analyst,
            "task_list": task_list.stock_analyst_task_list,
            "label": "STOCK",
        },
        {
            "agent": research_analyst,
            "task_list": task_list.research_analyst_task_list,
            "label": "RESEARCH",
        },
        {
            "agent": investment_lead,
            "task_list": task_list.investment_lead_task_list,
            "label": "INVESTMENT LEADER",
        },
    ],
)

workflow.run()
