"""External HTTP APIs to interact with 3rd party services."""

import yfinance as yf


def yFinance(query: str):
    """
    Search Yfinance for the given query and return text results.

    Args:
        query: The search symbol to query like MSFT

    Returns:
        Dictionaries containing search results
    """

    data = yf.Ticker(query)

    return data.info
