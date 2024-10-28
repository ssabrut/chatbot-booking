from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

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