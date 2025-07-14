from typing import List
from fastapi import FastAPI
from upsonic import Task
from upsonic.tools import Search

from workflow import Workflow, WorkflowEntry
from agents import stock_analyst, research_analyst, investment_lead
import tasks.list as task_list

app = FastAPI()

entries: List[WorkflowEntry] = [
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
]

workflow = Workflow(
    name="Investment Report Generator",
    description="Investment Report Generator Workflow Example with Upsonic",
    entries=entries,
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/generate-report")
async def generate_report(tickers: str):
    #! Implement this!
    summarized_response = workflow.run()

    return {"response": summarized_response}


@app.get("/ask")
async def ask(query: str):
    task = Task(query, tools=[Search])
    response = stock_analyst.do(task)
    return {"response": response}
