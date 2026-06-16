from aitool.client import AiClient


class ChatCommand:
    def __init__(self, client: AiClient):
        self.client = client

    def execute(self, model: str, prompt: str) -> str:
        response_text = self.client.send_response(model, prompt)
        return response_text
