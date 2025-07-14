from upsonic import Agent, Task
from typing import TypedDict, List
import time


class WorkflowEntry(TypedDict):
    agent: Agent
    task_list: list[Task]
    label: str


class Workflow:
    """
    Upsonic Workflow implementation for managing multiple agents.


    Args:
        name: Workflow name.
        description: Workflow description.
        entries: Workflow agent, task and label entries in a list.
            type: WorkflowEntry
        timeout: Timeout between executing next agent's task. (in seconds)
    """

    def __init__(
        self,
        name: str,
        description: str,
        entries: List[WorkflowEntry],
        timeout: int = 1,
    ):
        self.name: str = name
        self.description: str = description
        self.entries: List[WorkflowEntry] = entries
        self.timeout: int = timeout
        self.__summary: str = ""

    def run(self) -> None:
        """
        Runs the workflow in a loop with specified agents and tasks
        """

        for entry in self.entries:
            agent, tasks, label = entry["agent"], entry["task_list"], entry["label"]

            print(f"----{label}----")
            agent.do(tasks)
            time.sleep(self.timeout)

            # save agent task response and save it to summary
            # self.__summary += response
        # summarize it in the end of the workflow

        # self.__summarize()
        # return self.__summary

    def __summarize(self):
        summary = self.__summary

        # do something

        self.__summary = summary
