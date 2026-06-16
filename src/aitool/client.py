from abc import ABC, abstractmethod
from openai import OpenAI
from .models import ConfigModel

class AiClient(ABC):
    """Abstract base class for AI service providers."""
    
    @abstractmethod
    def send_message(self, prompt: str) -> str:
        """Send a message and return the response string."""
        pass

class OpenAiClient(AiClient):
    """OpenAI-compatible client implementation."""
    
    def __init__(self, config: ConfigModel):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url
        )

    def send_message(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.config.default_model,
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response.choices[0].message.content or ""

class FakeAiClient(AiClient):
    """A fake client for testing purposes."""
    
    def __init__(self, response: str = "4"):
        self.response = response
        self.last_prompt = None

    def send_message(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response
