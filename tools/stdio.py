"""
Host related tools like reading, creating files on the host machine.
"""

from typing import Literal
from datetime import datetime
from pathlib import Path


def writeContentToFile(
    file_path: str,
    content: str,
):
    """
    Write content to a file.

    Args:
        file_path: Path to the file to write to
        content: Content to write to the file

    Returns:
        An integer of writen bytes
    """

    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f"Content written to {file_path} successfully"
    except Exception as e:
        return f"Failed to write to file: {str(e)}"


class Reports:
    """
    Reports directory file read write operations.
    """

    @staticmethod
    def create_markdown_report(
        agent_role: Literal["stock-analyst", "research-analyst", "investment-lead"],
        content: str,
    ):
        """
        Creates a .md document in the correct directory with the date time string

        Args:
            agent_role:
                Must be one of stock-analyst, research-analyst, investment-lead.
                Only pass your own exact role value
            content: String content to write to file
        Returns:
            A message indicating success or failure
        """

        dir = Path("reports")

        # Check if it exists and is a directory
        if dir.exists() and dir.is_dir():
            for _ in dir.iterdir():
                pass
        else:
            print("Directory does not exist or is not a directory.")

        prefix = "demo_"  # Just for the demo

        if agent_role == "stock-analyst":
            pathname = f"{prefix}stock_analyst_report_{dateTimeString()}.md"
        elif agent_role == "research-analyst":
            pathname = f"{prefix}research_analyst_report_{dateTimeString()}.md"
        elif agent_role == "investment-lead":
            pathname = f"{prefix}investment_leader_report_{dateTimeString()}.md"
        else:
            pathname = f"{prefix}report{dateTimeString()}.md"

        dir = dir.joinpath(pathname)

        return dir.write_text(content, encoding="utf-8")


def dateTimeString() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")
