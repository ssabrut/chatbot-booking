from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

base_prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])