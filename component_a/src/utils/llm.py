import os
import logging
from schema.llm_schema import Turn

MODEL_ENDPOINT = os.environ.get("COMPONENT_A_LLM_HOST", "http://vllm:8000")
MODEL_NAME = os.environ.get("COMPONENT_A_MODEL_NAME", "model_name")

logging.basicConfig(level=logging.INFO)


class LLM:
    def __init__(self) -> None:
        """
        Initialize LLM
        """
        pass

    def chat(self, conversation: list[Turn]) -> Turn:
        """
        Converse with LLM

        Args:
            conversation: a list of turns that forms the conversation

        Returns:
            Turn: LLM's response
        """

        # TODO: Implement checks for validity of `conversation`
        logging.info(f"LLM received conversation {conversation}")

        response = Turn(role="assistant", content="How can I help you today?")
        return response
