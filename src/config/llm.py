from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1", temperature=0, max_tokens=100)