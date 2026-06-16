from rich.console import Console
from .client import AiClient


# opencode -s ses_130d3ca9fffe4LqdYQXvqd3Iuh
class ChatCommand:
    def __init__(self, client: AiClient):
        self.client = client
        self.console = Console()

    def execute(self, prompt: str) -> str:
        response_text = self.client.send_message(prompt)
        
        self.console.print(response_text)
        
        # Ensure a final newline if the response didn't end with one
        if not response_text.endswith("\n"):
            self.console.print()
            
        return response_text
