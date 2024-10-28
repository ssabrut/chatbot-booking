from src.config.memory import get_by_session_id
from src.config.prompt import base_prompt
from langchain_ollama import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory

llm = ChatOllama(model="llama3.1")
chain = base_prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_by_session_id,
    input_messages_key="input",
    history_messages_key="history"
)