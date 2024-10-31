from src.config.llm import llm
from langchain.chains.conversation.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)