from pydantic import BaseModel, Field
from typing import List, Optional

class ConfigModel(BaseModel):
    api_key: str = Field(default="ollama")
    base_url: str = Field(default="http://localhost:11434/v1")
    default_model: str = Field(default="llama3")

class Message(BaseModel):
    role: str
    content: str

class ChatCompletionSpec(BaseModel):
    model: str
    messages: List[Message]
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    stream: bool = True
