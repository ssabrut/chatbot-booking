from pydantic import BaseModel, Field
from typing import List
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage

class InMemoryHistory(BaseChatMessageHistory, BaseModel):
    """
    In-memory implementation of chat message history.

    Attributes
    ----------
    messages : List[BaseMessage]
        A list to store chat messages.

    Methods
    -------
    add_messages(messages: List[BaseMessage]) -> None
        Adds a list of messages to the history.
    get_session_history() -> List[BaseMessage]
        Returns the session history.
    clear() -> None
        Clears the message history.
    """

    messages: List[BaseMessage] = Field(default_factory=list)

    def add_messages(self, messages: List[BaseMessage]) -> None:
        """
        Adds a list of messages to the history.

        Parameters
        ----------
        messages : List[BaseMessage]
            The messages to add to the history.
        """
        self.messages.extend(messages)

    def get_session_history(self) -> List[BaseMessage]:
        """
        Returns the session history.

        Returns
        -------
        List[BaseMessage]
            The list of messages in the session history.
        """
        return self.messages

    def clear(self) -> None:
        """
        Clears the message history.
        """
        self.messages = []

memory = InMemoryHistory()