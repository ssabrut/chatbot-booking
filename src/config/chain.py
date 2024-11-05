from src.config.llm import llm
from src.config.memory import memory
from src.tools import *
from src.config.prompt import prompt
from langchain.agents import create_tool_calling_agent, AgentExecutor

tools = [set_name, set_number_of_people, set_date, set_time, set_special_requests, set_email, set_phone_number, create_booking]
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory)