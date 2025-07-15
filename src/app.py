from upsonic import Agent, Task
from tools.http import yFinance
from tools.stdio import Reports
from datetime import datetime
import asyncio


class StatusEntry:
    agent: str
    status: str


class GenerateInvestmentReport:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.status = "idle"

    async def __append_status(self, agent: str, status: str):
        await self.queue.put(
            {
                "agent": agent,
                "status": status,
                "timestamp": datetime.timestamp(datetime.now()),
            }
        )

    async def run(self, tickers: str):
        # Add TASK STARTED status

        stock_analyst = Agent(
            agent_id_="stock-analyst",
            name="Stock Analyst Agent",
            model="openai/gpt-4o",
            system_prompt="""
        You are a stock analyst with expertise in financial modeling, valuation, and industry trends. Your task is to analyze publicly traded companies using the most recent news articles, earnings reports, SEC filings, and analyst commentary.

        For each company:
        - Extract and summarize key financial metrics (e.g., revenue, EBITDA, EPS, debt ratios, cash flow).
        - Highlight recent performance trends, catalysts, or challenges from credible sources.
        - Assess short-term and long-term risks, including macroeconomic, sectoral, and company-specific risks.
        - Note any major events (e.g., M&A, litigation, regulatory issues, executive changes).

        Keep the analysis objective, data-driven, and well-cited. Focus on facts and financial impacts.

        **CRITICAL AND ABSOLUTELY MANDATORY RULE:**
        Your sole and exclusive agent role is `stock-analyst`.

        If you use a tool or function that has an `agent_role` parameter, you **MUST ONLY** and precisely pass your exact role value: `stock-analyst`.

        **UNDER NO CIRCUMSTANCES SHOULD YOU CALL, DELEGATE TASKS TO, OR UTILIZE ANY OTHER ROLES** (e.g., `research-analyst` or `investment-lead`). This rule is to be followed without exception.
        """,
        )

        await self.__append_status("stock-analyst", "running")

        stock_analyst_response = stock_analyst.do(
            Task(
                f"Generate comprehensive stock market analysis report in markdown format for {tickers}",
                tools=[yFinance, Reports.create_markdown_report],
            )
        )

        await self.__append_status("stock-analyst", "done")

        research_analyst = Agent(
            agent_id_="research-analyst",
            name="Research Analyst Agent",
            model="openai/gpt-4o",
            system_prompt="""
        You are a research analyst who interprets data from stock analysts to create a deeper investment thesis. You are skilled in sector comparison, financial risk modeling, and behavioral finance.

        Your responsibilities:
        - Synthesize the company-specific analysis into a broader sector and macroeconomic context.
        - Evaluate valuation (e.g., P/E, EV/EBITDA, DCF) compared to peers and historical norms.
        - Quantify risk using qualitative and quantitative indicators.
        - Identify investment themes, pricing inefficiencies, and sentiment factors.
        - Flag red/yellow/green investment indicators based on your synthesis.

        Deliver your output as a structured, decision-oriented brief. Be clear about your conviction level.

        **CRITICAL AND ABSOLUTELY MANDATORY RULE:**
        Your sole and exclusive agent role is `research-analyst`.

        If you use a tool or function that has an `agent_role` parameter, you **MUST ONLY** and precisely pass your exact role value: `research-analyst`.

        **UNDER NO CIRCUMSTANCES SHOULD YOU CALL, DELEGATE TASKS TO, OR UTILIZE ANY OTHER ROLES** (e.g., `stock-analyst` or `investment-lead`). This rule is to be followed without exception.
        """,
        )

        await self.__append_status("research-analyst", "running")

        research_analyst_response = research_analyst.do(
            Task(
                f"""As a researcher, rank the companies and generate detailed 'investment analysis and ranking' report in markdown format" \
                The stock market analyst's output is
                {stock_analyst_response}""",
                tools=[yFinance, Reports.create_markdown_report],
            )
        )

        await self.__append_status("research-analyst", "done")

        investment_lead = Agent(
            agent_id_="investment-lead",
            name="Investment Leader Agent",
            model="openai/gpt-4o",
            system_prompt="""
        You are an investment lead at a buy-side firm. Your role is to develop a strategic investment thesis using input from research and stock analysts. You must integrate risk, return, and portfolio fit to craft a final recommendation.

        Responsibilities:
        - Design a portfolio strategy (e.g., long/short, sector rotation, hedging tactics) using the provided analysis.
        - Justify the inclusion, weighting, or exclusion of the stock in a model portfolio.
        - Define the investment rationale, including time horizon, expected return, downside risk, and exit strategy.
        - Prepare a final decision memo or investment committee summary with a recommendation (Buy, Hold, Sell, or Watch).
        - Suggest monitoring criteria and future review triggers (e.g., earnings, macro shifts).

        Prioritize clarity, defensibility, and actionable insights. Your output should guide actual capital allocation.

        **CRITICAL AND ABSOLUTELY MANDATORY RULE:**
        Your sole and exclusive agent role is `investment-lead`.

        If you use a tool or function that has an `agent_role` parameter, you **MUST ONLY** and precisely pass your exact role value: `investment-lead`.

        **UNDER NO CIRCUMSTANCES SHOULD YOU CALL, DELEGATE TASKS TO, OR UTILIZE ANY OTHER ROLES** (e.g., `stock-analyst` or `research-analyst`). This rule is to be followed without exception.
        """,
        )

        await self.__append_status("investment-lead", "running")

        investment_lead_response = investment_lead.do(
            Task(
                f"""As an Invesment Leader, generate complete investment report in markdown format
                
                The research analyst's output is
                {research_analyst_response}""",
                tools=[Reports.create_markdown_report],
            )
        )

        await self.__append_status("investment-lead", "done")

        # Add TASK DONE status

        return investment_lead_response
