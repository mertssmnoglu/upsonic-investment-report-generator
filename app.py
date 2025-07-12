import tasks.list as task_list
import time

# Agents
from agents import stock_analyst
from agents import research_analyst
from agents import investment_lead


# Workflow
print("----STOCK----")
stock_analyst.do(task_list.stock_analyst)
time.sleep(3)

print("----RESEARCH----")
research_analyst.do(task_list.research_analyst)
time.sleep(3)

print("----INVESTMENT LEADER----")
investment_lead.do(task_list.investment_lead)
