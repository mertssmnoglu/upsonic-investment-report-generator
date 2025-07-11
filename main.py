from fastapi import FastAPI
from upsonic import Task
from upsonic.tools import Search
from agents import agent

app = FastAPI()


@app.get("/ask")
async def ask(query: str):
    task = Task(query, tools=[Search])
    response = agent.do(task)
    return {"response": response}
