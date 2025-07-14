from upsonic import Agent
import system_prompts

stock_analyst = Agent(
    agent_id_="stock-analyst",
    name="Stock Analyst Agent",
    model="openai/gpt-4o",
    system_prompt=system_prompts.stock_analyst,
)

research_analyst = Agent(
    agent_id_="research-analyst",
    name="Research Analyst Agent",
    model="openai/gpt-4o",
    system_prompt=system_prompts.research_analyst,
)

investment_lead = Agent(
    agent_id_="investment-lead",
    name="Investment Leader Agent",
    model="openai/gpt-4o",
    system_prompt=system_prompts.investment_lead,
)
