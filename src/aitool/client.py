from abc import ABC, abstractmethod
from typing import Iterable
from openai import OpenAI
from .models import ConfigModel

class AiClient(ABC):
    """Abstract base class for AI service providers."""
    
    @abstractmethod
    def send_message(self, prompt: str) -> Iterable[str]:
        """Stream chat completion chunks as strings."""
        pass

class OpenAiClient(AiClient):
    """OpenAI-compatible client implementation."""
    
    def __init__(self, config: ConfigModel):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url
        )

    def send_message(self, prompt: str) -> Iterable[str]:
        stream = self.client.chat.completions.create(
            model=self.config.default_model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

class FakeAiClient(AiClient):
    """A fake client for testing purposes."""
    
    def __init__(self, response: str = "4"):
        self.response = response
        self.last_prompt = None

    def send_message(self, prompt: str) -> Iterable[str]:
        self.last_prompt = prompt
        yield self.response
