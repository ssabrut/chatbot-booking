from src.config.llm import llm
from src.config.memory import memory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# Define your custom prompt
custom_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""You are a virtual assistant responsible for taking restaurant reservations. Your task is to collect the following information:
- Name
- Number of people
- Date
- Time
- Special requests (if any)

Provide a confirmation after you have all the required details. Keep your responses short and concise. Do not include any irrelevant information or make the text unnecessarily long.

History:
{history}

Curent Conversation:
Human: {input}
AI:"""
)

chain = ConversationChain(
    llm=llm,
    verbose=True,
    memory=memory,
    prompt=custom_prompt
)