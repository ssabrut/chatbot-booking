from pydantic import BaseModel, Field
from typing import List
from langchain_community.memory.kg import ConversationKGMemory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You're an assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

llm = ChatOllama(model="llama3.1")

memory = InMemoryHistory()
chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    memory.get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

def run():
    memory.add_message(AIMessage(content="hello"))
    print(memory)

if __name__ == "__main__":
    run()