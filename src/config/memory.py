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

    def clear(self) -> None:
        """
        Clears the message history.
        """
        self.messages = []

store = {}

def get_by_session_id(session_id: str) -> BaseChatMessageHistory:
    """
    Retrieves the chat message history for a given session ID.

    If the session ID does not exist in the store, a new `InMemoryHistory` instance is created and stored.

    Parameters
    ----------
    session_id : str
        The session ID for which to retrieve the chat message history.

    Returns
    -------
    BaseChatMessageHistory
        The chat message history associated with the given session ID.
    """
    if session_id not in store:
        store[session_id] = InMemoryHistory()
    return store[session_id]