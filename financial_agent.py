from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# web search agent
web_serach_agent = Agent(
    name="WebSearchAgent",
    role="Search the web for the information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


# financial agent
finance_agent = Agent(
    name="FinanceAgent",
    role="Get financial information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)], 
    instructions=["Use tables to show the data"],
    show_tool_calls=True,
    markdown =True,
)

multi_ai_agent=Agent(
    team=[web_serach_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to show the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summerize the analyst recommendations and share the latest news for Apple Inc. (AAPL).", stream=True)