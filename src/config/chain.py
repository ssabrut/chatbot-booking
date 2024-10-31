from src.config.llm import llm
from src.config.memory import memory
from src.tools import tools
from src.config.prompt import prompt
from langchain.agents import create_tool_calling_agent, AgentExecutor

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory)