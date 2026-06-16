from abc import ABC, abstractmethod
from openai import OpenAI


class AiClient(ABC):
    """Abstract base class for AI service providers."""
    
    @abstractmethod
    def send_response(self, model: str, prompt: str) -> str:
        """Send a message and return the response string."""
        pass

class OpenAiClient(AiClient):
    """OpenAI-compatible client implementation."""
    
    def __init__(
        self, 
        api_key: str, 
        base_url: str, 
        default_model: str
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.default_model = default_model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def send_response(self, model: str, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response.choices[0].message.content or ""

class FakeAiClient(AiClient):
    """A fake client for testing purposes."""
    
    def __init__(self):
        self.prompt_responses: dict[tuple[str, str], str] = {}

    def send_response(self, model: str, prompt: str) -> str:
        if (model, prompt) in self.prompt_responses:
            return self.prompt_responses[(model, prompt)]
        raise ValueError(f"No response configured for model '{model}' and prompt '{prompt}'")

    def add_response(self, model: str, prompt: str, response: str) -> None:
        self.prompt_responses[(model, prompt)] = response
