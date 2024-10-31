from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1", temperature=.6, max_tokens=128)