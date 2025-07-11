import yfinance as yf


def YFinanceTool(query: str):
    """
    Search Yfinance for the given query and return text results.

    Args:
        query: The search symbol to query like MSFT

    Returns:
        Dictionaries containing search results
    """

    print(query)
    data = yf.Ticker(query)

    return data.info


def WriteContentToFile(
    file_path: str,
    content: str,
):
    """
    Write content to a file.

    Args:
        file_path: Path to the file to write to
        content: Content to write to the file

    Returns:
        A message indicating success or failure
    """

    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f"Content written to {file_path} successfully"
    except Exception as e:
        return f"Failed to write to file: {str(e)}"


stdio_tools = [WriteContentToFile]
"""
Hosts related tools like reading, creating files on the host machine.
"""

http_apis = [YFinanceTool]
"""
External HTTP APIs to interact with 3rd party services.
"""
