from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from .client import AiClient


# opencode -s ses_130d3ca9fffe4LqdYQXvqd3Iuh
class ChatCommand:
    def __init__(self, client: AiClient):
        self.client = client
        self.console = Console()

    def execute(self, prompt: str) -> str:
        response_text = ""

        # Use Live to update the markdown as it streams
        with Live(Markdown(""), refresh_per_second=10, console=self.console) as live:
            for chunk in self.client.send_message(prompt):
                response_text += chunk
                live.update(Markdown(response_text))

        # Ensure a final newline if the stream didn't end with one
        if not response_text.endswith("\n"):
            self.console.print()

        return response_text
