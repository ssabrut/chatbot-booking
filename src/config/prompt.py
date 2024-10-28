from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful assistant that helps people with their bookings."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])