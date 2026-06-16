from abc import ABC, abstractmethod
from dataclasses import dataclass
from openai import OpenAI


@dataclass
class OpenAiClientConfig:
    api_key: str
    endpoint: str
    model: str


class AiClient(ABC):
    """Abstract base class for AI service providers."""
    
    @abstractmethod
    def send_response(self, model: str, prompt: str) -> str:
        """Send a message and return the response string."""
        pass

class OpenAiClient(AiClient):
    """OpenAI-compatible client implementation."""
    
    def __init__(self, config: OpenAiClientConfig):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.endpoint
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
