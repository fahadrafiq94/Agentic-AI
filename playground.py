from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os 
import phi 
from phi.playground import Playground, serve_playground_app

# Load the environmental variables from .env file
load_dotenv()

phi.api = os.getenv("PHI_API_kEY")

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

app = Playground(agents=[web_serach_agent, finance_agent]).get_app()

if __name__ == "__main__":
    # Run the playground app
    # "filename:app" is the name of the file and the variable that holds the FastAPI app
    serve_playground_app("playground:app", reload=True)
